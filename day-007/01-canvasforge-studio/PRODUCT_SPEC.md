# CanvasForge Studio — MVP Specification

## Audience
Students, independent creators, social media managers, and small businesses that need simple visual assets quickly.

## Core workflow
1. Start a project and choose a canvas preset.
2. Choose a template or start blank.
3. Add text, shapes, and images.
4. Adjust object appearance and layer order.
5. Save locally and export a PNG.

## Canvas presets
- Instagram post — 1080 × 1080
- Instagram story — 1080 × 1920
- YouTube thumbnail — 1280 × 720
- Presentation — 1920 × 1080
- Custom dimensions

## Editor layout
- Top toolbar: project name, undo/redo, zoom, save, export.
- Left tool rail: select, text, shapes, image import.
- Center: editable design canvas with selection handles and optional grid.
- Right inspector: properties for the selected object.
- Layers: visibility, lock, rename, reorder, delete.
- AI helper: palette and headline suggestions. Never imply an external model is running unless configured.

## Acceptance criteria
- Adding text and shapes changes the editable document.
- Selecting an object reveals its properties.
- Delete and duplicate affect the selected object.
- Undo/redo restore previous document states.
- Reloading restores a locally saved project.
- PNG export uses document dimensions rather than screen-preview dimensions.
- Template elements remain individually editable.
- Empty states and unavailable features are explicit.
- No fabricated metrics or nonfunctional controls presented as complete.

## First-MVP non-goals
- Full Photoshop/Illustrator parity.
- Professional RAW image processing.
- Cloud collaboration and multi-user editing.
- AI image generation without a configured provider.
- Production-grade background removal without a configured service.
