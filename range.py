for i in widthRange:
    for j in heightRange:
        r, g, b=rgb_im.getpixel((i, j))
        h, s,v=colorsys.rgb_to_hsv(r/255.0, g/255.0, b/255.0)
        h=h *360
        int(round(h))
        print(h)
