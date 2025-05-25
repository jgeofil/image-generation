import replicate
import os
from dotenv import load_dotenv

load_dotenv()
# Load environment variables from .env file
REPLICATE_API_TOKEN = os.getenv("REPLICATE_API_TOKEN")
if not REPLICATE_API_TOKEN:
    raise ValueError("REPLICATE_API_TOKEN environment variable not set.")
# The REPLICATE_API_TOKEN environment variable is already set above, which is sufficient for the replicate package.


def generate_image(
    prompt, model="black-forest-labs/flux-schnell", width=512, height=512
):
    """
    Generate an image using the specified model and parameters.

    Args:
        prompt (str): The text prompt to generate the image from.
        model (str): The model to use for image generation.
        width (int): The width of the generated image.
        height (int): The height of the generated image.

    Returns:
        str: The URL of the generated image.
    """
    output = replicate.run(
        model,
        input={
            "prompt": prompt,
            "width": width,
            "height": height,
            "output_format": "webp",
        },
    )
    return output


if __name__ == "__main__":
    # Example usage
    prompt = "A futuristic city skyline at sunset"
    model = "black-forest-labs/flux-schnell"
    width = 512
    height = 512
    output = generate_image(prompt, model, width, height)

    # Convert the iterator to a list to access the first element
    output_list = list(output)
    with open("output.webp", "wb") as f:
        f.write(output_list[0].read())
