text = "qwertyuiopasdfghjklzxcvbnm"
fonts = ["🅠🅦🅔🅡🅣🅨🅤🅘🅞🅟🅐🅢🅓🅕🅖🅗🅙🅚🅛🅩🅧🅒🅥🅑🅝🅜","🅀🅆🄴🅁🅃🅈🅄🄸🄾🄿🄰🅂🄳🄵🄶🄷🄹🄺🄻🅉🅇🄲🅅🄱🄽🄼","𝕢𝕨𝕖𝕣𝕥𝕪𝕦𝕚𝕠𝕡𝕒𝕤𝕕𝕗𝕘𝕙𝕛𝕜𝕝𝕫𝕩𝕔𝕧𝕓𝕟𝕞","𐌒Ꮤ𐌄𐌓𐌕𐌙𐌵𐌉Ꝋ𐌐𐌀𐌔𐌃𐌅Ᏽ𐋅Ꮭ𐌊𐌋Ɀ𐋄𐌂ᕓ𐌁𐌍𐌌","𝓺𝔀𝓮𝓻𝓽𝔂𝓾𝓲𝓸𝓹𝓪𝓼𝓭𝓯𝓰𝓱𝓳𝓴𝓵𝔃𝔁𝓬𝓿𝓫𝓷𝓶","ᎤᏇᏋᏒᏖᎩᏬᎥᎧᎮᏗᏕᎴᎦᎶᏂᏠᏦᏝፚጀፈᏉᏰᏁᎷ","𝖖𝖜𝖊𝖗𝖙𝖞𝖚𝖎𝖔𝖕𝖆𝖘𝖉𝖋𝖌𝖍𝖏𝖐𝖑𝖟𝖝𝖈𝖛𝖇𝖓𝖒","ｑｗｅｒｔｙｕｉｏｐａｓｄｆｇｈｊｋｌｚｘｃｖｂｎｍ","զաɛʀȶʏʊɨօքǟֆɖʄɢɦʝӄʟʐӼƈʋɮռʍ","𝖖𝖜𝖊𝖗𝖙𝖞𝖚𝖎𝖔𝖕𝖆𝖘𝖉𝖋𝖌𝖍𝖏𝖐𝖑𝖟𝖝𝖈𝖛𝖇𝖓𝖒✍"]
emoji = "🍳🔱𝓔🌱🍄🏋⛎🕴😀🅿🅰💲🐬🔩🐋♓🎷🎉👢💤❎🌜✌🅱🥄Ⓜ"
import random

def nick_generator(name):
    result = []
    for font in fonts:
        my_name = name
        for i in range(len(text)):
            my_name = my_name.replace(text[i],font[i])
        e = random.choice(emoji)
        result.append(e+my_name+e)
    return result

