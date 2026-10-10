# AI Industrial Defect Detection

Computer-vision inspection prototype for identifying potential manufacturing defects in product images. Includes a YOLO inference pipeline, Streamlit dashboard, configurable review policy, CSV export, and tests.

> This is a portfolio scaffold, not a trained industrial defect detector. A custom YOLO model trained on labeled examples from the target production line is required for meaningful defect detection. General-purpose pretrained weights do not automatically detect scratches or cracks.

## Example workflow
1. Upload a product image.
2. Run the configured YOLO model.
3. Overlay detections and confidence scores.
4. Mark the inspection PASS or REVIEW based on configured defect labels.
5. Export inspection history to CSV.

## Quick start
Python 3.10–3.12 recommended.

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
pytest
streamlit run app/streamlit_app.py
```

## Configure custom weights
Set `DEFECT_MODEL_PATH` to a trained YOLO `.pt` file and optionally set `DEFECT_CONFIDENCE` and `DEFECT_LABELS`. See `.env.example`. Do not commit proprietary images or large model weights to a public repo.

## Architecture
Image upload → YOLO inference → normalized detections → decision policy → annotated image + inspection record → dashboard / CSV.

## Training workflow
- Collect representative images under production-like lighting and camera conditions.
- Define a consistent defect taxonomy and label examples.
- Split by batch/session to reduce data leakage.
- Train a domain-specific detector and evaluate precision, recall, mAP, and false-negative rate by class.
- Select thresholds with quality engineers and validate before deployment.

Example labels are `scratch`, `crack`, `dent`, and `contamination`; adapt them to the product and dataset.

## Decision semantics
- `REVIEW`: a configured defect label exceeds the confidence threshold.
- `PASS`: no configured defect label exceeds the threshold. This is not a guarantee that a part is defect-free.
- Missing weights: inference cannot run and the UI reports the configuration issue.

## Limitations
No trained model, PLC/MES integration, automated reject mechanism, or production guarantee is included. Treat this as a portfolio demo, not a safety-critical quality gate.
