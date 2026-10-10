import pandas as pd
import streamlit as st
from app.config import load_settings
from app.inference import load_image_rgb, run_yolo_inference
from app.policy import decide_inspection
from app.records import build_record, records_to_csv

st.set_page_config(page_title="AI Industrial Defect Detection", page_icon="🏭", layout="wide")
settings = load_settings()
st.title("🏭 AI Industrial Defect Detection")
st.caption("Inspection prototype • Custom-trained defect weights required for meaningful results")
with st.sidebar:
    st.header("Inspection settings")
    confidence = st.slider("Confidence threshold", 0.0, 1.0, settings.confidence, 0.05)
    raw = st.text_input("Defect labels (comma-separated)", ", ".join(sorted(settings.defect_labels)))
    defect_labels = {x.strip().lower() for x in raw.split(",") if x.strip()}
    st.code(settings.model_path)
    st.warning("General-purpose YOLO weights are not a substitute for a domain-trained defect model.")
if "inspection_records" not in st.session_state:
    st.session_state.inspection_records = []
upload = st.file_uploader("Upload a product image", type=["png", "jpg", "jpeg", "webp"])
if upload is None:
    st.markdown("### Workflow")
    st.write("Upload an image → run inference → review flagged detections → export records.")
    st.info("Set DEFECT_MODEL_PATH to your custom-trained YOLO .pt weights to enable inference.")
else:
    image = load_image_rgb(upload)
    left, right = st.columns(2)
    left.image(image, caption="Input image", use_container_width=True)
    try:
        detections, annotated = run_yolo_inference(image, settings.model_path, confidence)
        decision = decide_inspection(detections, defect_labels, confidence)
        st.session_state.inspection_records.append(build_record(upload.name, detections, decision))
        right.image(annotated, caption="Annotated image", use_container_width=True)
        if decision.status == "REVIEW":
            st.error("REVIEW — " + ", ".join(decision.flagged_labels))
        else:
            st.success("PASS — no configured defect labels flagged")
        st.caption(decision.reason)
        if detections:
            st.dataframe(pd.DataFrame([
                {"Label": d.label, "Confidence": round(d.confidence, 3),
                 "X1": round(d.x1, 1), "Y1": round(d.y1, 1),
                 "X2": round(d.x2, 1), "Y2": round(d.y2, 1)}
                for d in detections
            ]), use_container_width=True)
    except FileNotFoundError as exc:
        st.error(str(exc))
    except Exception as exc:
        st.exception(exc)
st.divider()
st.subheader("Inspection history (this session)")
records = st.session_state.inspection_records
if records:
    frame = pd.DataFrame(records)
    c1, c2, c3 = st.columns(3)
    c1.metric("Inspections", len(frame))
    c2.metric("Review required", int((frame["status"] == "REVIEW").sum()))
    c3.metric("Pass rate", f'{(frame["status"] == "PASS").mean() * 100:.1f}%')
    st.dataframe(frame, use_container_width=True)
    st.download_button("Download inspection CSV", records_to_csv(records),
                       "inspection_records.csv", "text/csv")
else:
    st.caption("No inspection records yet.")
