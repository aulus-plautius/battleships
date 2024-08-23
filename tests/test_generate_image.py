from lib.generate_image import GenerateImage
"""
Given an Image object
image.hit returns image
"""

def test_image_hit():
    image = GenerateImage()
    assert image.hit == "\n".join( [r"    0 1 2 3 4 5 6 7 8 9  ",
                                    r"  ┌─────────────────────┐",
                                    r"A │  _.-^^---....,,--_  │",
                                    r"B │_-                 -_│",
                                    r"C │<        HIT!      >)│",
                                    r"D │\.                 / │",
                                    r"E │  ```--. . , ; .--'  │",  
                                    r"F │         | |   |     │",   
                                    r"G │     .-=||  | |=-.   │",
                                    r"H │     `-=#$%&%$#=-'   │",
                                    r"I │         | ;  :|     │",
                                    r"J │___.-#%&$@%#&#~,.____│",
                                    r"  └─────────────────────┘"])
    
def test_image_sink():
    image = GenerateImage()
    assert image.sink == "\n".join([r"    0 1 2 3 4 5 6 7 8 9  ",
                                    r"  ┌─────────────────────┐",
                                    r"A │       HIT!          │",
                                    r"B │              ( )    │",  
                                    r"C │ BOOM!*  __*___|_ *  │",
                                    r"D │   *  _ |_________*  │",
                                    r"E │====| | |* SINK!   | │",
                                    r"F │.--*------------*----│",
                                    r"G │ \      *        *  /│",
                                    r"H │  \________________/ │",
                                    r"I │~~~~~~~~~~~~~~~~~~~~~│",
                                    r"J │  ~~~~~~~~~~~~~~~~~~~│",
                                    r"  └─────────────────────┘"])


def test_image_miss():
    image = GenerateImage()
    assert image.miss == "\n".join(["    0 1 2 3 4 5 6 7 8 9  ",
                                    "  ┌─────────────────────┐",
                                    "A |                     |",
                                    "B │       .-- .         │",
                                    "C │     .(     )        │",
                                    "D │   (       ))     _  │",
                                    "E │  _ `- __.'    . ` ) │",
                                    "F │  __ .  MISS! :(    )│",
                                    "G │(     '`. .  `(     )│",
                                    "H │(       ) )    ` _.' │",
                                    "I │ `_.:'-'             │",
                                    "J │~~~~~~~~~~~~~~~~~~~~~│",
                                    "  └─────────────────────┘"])
