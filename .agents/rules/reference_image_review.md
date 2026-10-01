# Mandatory Reference Image Human Review Gate

## Rule
Whenever an AI reference image or costume/wardrobe reference is generated (e.g. via FLUX, Recraft, Imagen, or image edit tools) to be used as input conditioning for a downstream video generation task (e.g. Seedance, Kling, Hailuo/MiniMax, VEO, LTX):

1. **Do NOT automatically proceed to video generation.**
2. **Present the generated reference image(s) directly to the user** with a clickable link and visual preview.
3. **Explicitly ask for human approval / review** of the reference image's subject identity, costume details, colors, and proportions.
4. **Wait for explicit user confirmation** before submitting the downstream video generation job.
