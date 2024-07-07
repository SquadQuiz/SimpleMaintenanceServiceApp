from songline import Sendline

token = 'jmJ49DfTEpMYwMVIlg42qMHBiMtmiFaPpmqB7gNSPHX'
messenger = Sendline(token)

messenger.sendtext("How are u?")
messenger.sticker(105, 1)
messenger.sendimage('https://png.pngtree.com/png-clipart/20190504/ourmid/pngtree-pink-hello-saturday-typography-3d-lettering.jpg')

