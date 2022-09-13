import os
import random


from PIL import Image, ImageDraw, ImageFont


class MemeEngine:
    '''Instance of theis class will generate memes to a given directory

    Argument:
        out_path (str) : Needed to save generated meme.
    '''

    def __init__(self, meme_dir: str):
        '''Instantiate MemeGenerator with path str.

        Argument:
            meme_dir (str) : Path where to save image.
        '''
        self.meme_dir = meme_dir
        self.count = 1
        if not os.path.exists(meme_dir):
            os.makedirs(meme_dir)

    '''Define meme format attributes'''
    meme_fill = 'white'  # Text fill color
    meme_factor = 18  # Font scale smalller relative to width
    meme_font = './arial.ttf'  # truetype font of the meme

    def make_meme(self, img_path: str, body: str, author: str,
                  width: int = 500) -> str:
        '''Generate meme and return file path of meme.

        Method will generate meme with 'text' as a caption that is written by
        'author'.

        Arguments:
            img_path (str) -- Path of image.
            body (str) -- Caption text.
            author (str) -- Author name.
            width (int) -- Desired width of final image while keeping aspect
                            ratio.

        Returns:
            out_path -- Path to save image of generated meme
        '''
        caption = f'{body}, {author}'

        with Image.open(img_path) as meme_image:
            # Resize image to be 500px wide while keeping aspect ratio
            old_width, old_height = meme_image.size
            scale = width/old_width
            new_size = new_width, new_height = width, int(scale*old_height)
            meme_image = meme_image.resize(new_size)

            # Add caption to meme_image
            draw_quote = ImageDraw.Draw(meme_image)
            font_size = width//self.meme_factor
            x, y = 10, random.randint(font_size, new_height-font_size)
            font = ImageFont.truetype(font=self.meme_font, size=font_size)
            draw_quote.text((x, y), caption, fill=self.meme_fill, font=font)

            # Save meme to out_path made by MemeEngine object
            meme_name = f'meme_{img_path.split("/")[-1]}'
            out_path = f'{self.meme_dir}/{meme_name}'
            meme_image.save(out_path)

        return out_path
