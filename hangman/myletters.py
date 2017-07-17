'''
Each font is 11 x 7
Example, paper = |, ink = ' '
'''
def magnify_letter_a(row,paper,ink):
    '''
    ||||||||||| 11p
    ||||| ||||| 5p,1i,5p
    ||||   |||| 4p,3i,4p
    |||  |  ||| 3p,2i,1p,2i,3p
    ||       || 2p,7i,2p
    || ||||| || 2p,1i,5p,1i,2p
    ||||||||||| 11p
    '''
    if(row == 1):
        return 11*paper
    elif(row == 2):
        return 5*paper+1*ink+5*paper
    elif(row == 3):
        return 4*paper+3*ink+4*paper
    elif(row == 4):
        return 3*paper+2*ink+1*paper+2*ink+3*paper
    elif(row == 5):
        return 2*paper+7*ink+2*paper
    elif(row == 6):
        return 2*paper+1*ink+5*paper+1*ink+2*paper
    elif(row == 7):
        return 11*paper
def magnify_letter_b(row,paper,ink):
    '''
    ||||||||||| 11p
    ||    ||||| 2p,4i,5p
    ||   |  ||| 2p,3i,1p,2i,3p
    ||     |||| 2p,5i,4p
    ||   |  ||| 2p,3i,1p,2i,3p
    ||    ||||| 2p,4i,5p
    ||||||||||| 11p
    '''
    if(row == 1):
        return 11*paper
    elif(row == 2):
        return 2*paper+4*ink+5*paper
    elif(row == 3):
        return 2*paper+3*ink+1*paper+2*ink+3*paper
    elif(row == 4):
        return 2*paper+5*ink+4*paper
    elif(row == 5):
        return 2*paper+3*ink+1*paper+2*ink+3*paper
    elif(row == 6):
        return 2*paper+4*ink+5*paper
    elif(row == 7):
        return 11*paper
def magnify_letter_c(row,paper,ink):
    '''
    ||||||||||| 11p
    |||     ||| 3p,5i,3p
    ||  ||||||| 2p,2i,7p
    || |||||||| 2p,1i,8p
    ||  ||||||| 2p,2i,7p
    |||     ||| 3p,5i,3p
    ||||||||||| 11p
    '''
    if(row == 1):
        return 11*paper
    elif(row == 2):
        return 3*paper+5*ink+3*paper
    elif(row == 3):
        return 2*paper+2*ink+7*paper
    elif(row == 4):
        return 2*paper+1*ink+8*paper
    elif(row == 5):
        return 2*paper+2*ink+7*paper
    elif(row == 6):
        return 3*paper+5*ink+3*paper
    elif(row == 7):
        return 11*paper
def magnify_letter_d(row,paper,ink):
    '''
    ||||||||||| 11p
    ||     |||| 2p,5i,4p
    || |||| ||| 2p,1i,4p,1i,3p
    || |||| ||| 2p,1i,4p,1i,3p
    || |||| ||| 2p,1i,4p,1i,3p
    ||     |||| 2p,5i,4p
    ||||||||||| 11p
    '''
    if(row == 1):
        return 11*paper
    elif(row == 2):
        return 2*paper+5*ink+4*paper
    elif(row == 3):
        return 2*paper+1*ink+4*paper+1*ink+3*paper
    elif(row == 4):
        return 2*paper+1*ink+4*paper+1*ink+3*paper
    elif(row == 5):
        return 2*paper+1*ink+4*paper+1*ink+3*paper
    elif(row == 6):
        return 2*paper+5*ink+4*paper
    elif(row == 7):
        return 11*paper
def magnify_letter_e(row,paper,ink):
    '''
    ||||||||||| 11p
    ||       || 2p,7i,2p
    || |||||||| 2p,1i,8p
    ||     |||| 2p,5i,4p
    || |||||||| 2p,1i,8p
    ||       || 2p,7i,2p
    ||||||||||| 11p
    '''
    if(row == 1):
        return 11*paper
    elif(row == 2):
        return 2*paper+7*ink+2*paper
    elif(row == 3):
        return 2*paper+1*ink+8*paper
    elif(row == 4):
        return 2*paper+5*ink+4*paper
    elif(row == 5):
        return 2*paper+1*ink+8*paper
    elif(row == 6):
        return 2*paper+7*ink+2*paper
    elif(row == 7):
        return 11*paper
def magnify_letter_f(row,paper,ink):
    '''
    ||||||||||| 11p
    ||       || 2p,7i,2p
    || |||||||| 2p,1i,8p
    ||     |||| 2p,5i,4p
    || |||||||| 2p,1i,8p
    || |||||||| 2p,1i,8p
    ||||||||||| 11p
    '''
    if(row == 1):
        return 11*paper
    elif(row == 2):
        return 2*paper+7*ink+2*paper
    elif(row == 3):
        return 2*paper+1*ink+8*paper
    elif(row == 4):
        return 2*paper+5*ink+4*paper
    elif(row == 5):
        return 2*paper+1*ink+8*paper
    elif(row == 6):
        return 2*paper+1*ink+8*paper
    elif(row == 7):
        return 11*paper
def magnify_letter_g(row,paper,ink):
    '''
    ||||||||||| 11p
    ||      ||| 2p,6i,3p
    || |||||||| 2p,1i,8p
    || ||   ||| 2p,1i,2p,3i,3p
    || |||| ||| 2p,1i,4p,1i,3p
    ||      ||| 2p,6i,3p
    ||||||||||| 11p
    '''
    if(row == 1):
        return 11*paper
    elif(row == 2):
        return 2*paper+6*ink+3*paper
    elif(row == 3):
        return 2*paper+1*ink+8*paper
    elif(row == 4):
        return 2*paper+1*ink+2*paper+3*ink+3*paper
    elif(row == 5):
        return 2*paper+1*ink+4*paper+1*ink+3*paper
    elif(row == 6):
        return 2*paper+6*ink+3*paper
    elif(row == 7):
        return 11*paper
def magnify_letter_h(row,paper,ink):
    '''
    ||||||||||| 11p
    || ||||| || 2p,1i,5p,1i,2p
    || ||||| || 2p,1i,5p,1i,2p
    ||       || 2p,7i,2p
    || ||||| || 2p,1i,5p,1i,2p
    || ||||| || 2p,1i,5p,1i,2p
    ||||||||||| 11p
    '''
    if(row == 1):
        return 11*paper
    elif(row == 2):
        return 2*paper+1*ink+5*paper+1*ink+2*paper
    elif(row == 3):
        return 2*paper+1*ink+5*paper+1*ink+2*paper
    elif(row == 4):
        return 2*paper+7*ink+2*paper
    elif(row == 5):
        return 2*paper+1*ink+5*paper+1*ink+2*paper
    elif(row == 6):
        return 2*paper+1*ink+5*paper+1*ink+2*paper
    elif(row == 7):
        return 11*paper
def magnify_letter_i(row,paper,ink):
    '''
    ||||||||||| 11p
    |||     ||| 3p,5i,3p
    ||||| ||||| 5p,1i,5p
    ||||| ||||| 5p,1i,5p
    ||||| ||||| 5p,1i,5p
    |||     ||| 3p,5i,3p
    ||||||||||| 11p
    '''
    if(row == 1):
        return 11*paper
    elif(row == 2):
        return 3*paper+5*ink+3*paper
    elif(row == 3):
        return 5*paper+1*ink+5*paper
    elif(row == 4):
        return 5*paper+1*ink+5*paper
    elif(row == 5):
        return 5*paper+1*ink+5*paper
    elif(row == 6):
        return 3*paper+5*ink+3*paper
    elif(row == 7):
        return 11*paper
def magnify_letter_j(row,paper,ink):
    '''
    ||||||||||| 11p
    ||||||   || 6p,3i,2p
    ||||||| ||| 7p,1i,3p
    ||||||| ||| 7p,1i,3p
    ||| ||| ||| 3p,1i,3p,1i,3p
    ||||   |||| 4p,3i,4p
    ||||||||||| 11p
    '''
    if(row == 1):
        return 11*paper
    elif(row == 2):
        return 6*paper+3*ink+2*paper
    elif(row == 3):
        return 7*paper+1*ink+3*paper
    elif(row == 4):
        return 7*paper+1*ink+3*paper
    elif(row == 5):
        return 3*paper+1*ink+3*paper+1*ink+3*paper
    elif(row == 6):
        return 4*paper+3*ink+4*paper
    elif(row == 7):
        return 11*paper
def magnify_letter_k(row,paper,ink):
    '''
    ||||||||||| 11p
    || |||| ||| 2p,1i,4p,1i,3p
    || || ||||| 2p,1i,2p,1i,5p
    ||  ||||||| 2p,2i,7p
    || || ||||| 2p,1i,2p,1i,5p
    || |||| ||| 2p,1i,4p,1i,3p
    ||||||||||| 11p
    '''
    if(row == 1):
        return 11*paper
    elif(row == 2):
        return 2*paper+1*ink+4*paper+1*ink+3*paper
    elif(row == 3):
        return 2*paper+1*ink+2*paper+1*ink+5*paper
    elif(row == 4):
        return 2*paper+2*ink+7*paper
    elif(row == 5):
        return 2*paper+1*ink+2*paper+1*ink+5*paper
    elif(row == 6):
        return 2*paper+1*ink+4*paper+1*ink+3*paper
    elif(row == 7):
        return 11*paper
def magnify_letter_l(row,paper,ink):
    '''
    ||||||||||| 11p
    ||| ||||||| 3p,1i,7p
    ||| ||||||| 3p,1i,7p
    ||| ||||||| 3p,1i,7p
    ||| ||||||| 3p,1i,7p
    |||     ||| 3p,5i,3p
    ||||||||||| 11p
    '''
    if(row == 1):
        return 11*paper
    elif(row == 2):
        return 3*paper+1*ink+7*paper
    elif(row == 3):
        return 3*paper+1*ink+7*paper
    elif(row == 4):
        return 3*paper+1*ink+7*paper
    elif(row == 5):
        return 3*paper+1*ink+7*paper
    elif(row == 6):
        return 3*paper+5*ink+3*paper
    elif(row == 7):
        return 11*paper
def magnify_letter_m(row,paper,ink):
    '''
    ||||||||||| 11p
    || ||||| || 2p,1i,5p,1i,2p
    || | | | || 2p,1i,1p,1i,1p,1i,1p,1i,2p
    || || || || 2p,1i,2p,1i,2p,1i,2p
    || ||||| || 2p,1i,5p,1i,2p
    || ||||| || 2p,1i,5p,1i,2p
    ||||||||||| 11p
    '''
    if(row == 1):
        return 11*paper
    elif(row == 2):
        return 2*paper+1*ink+5*paper+1*ink+2*paper
    elif(row == 3):
        return 2*paper+1*ink+1*paper+1*ink+1*paper+1*ink+1*paper+1*ink+2*paper
    elif(row == 4):
        return 2*paper+1*ink+2*paper+1*ink+2*paper+1*ink+2*paper
    elif(row == 5):
        return 2*paper+1*ink+5*paper+1*ink+2*paper
    elif(row == 6):
        return 2*paper+1*ink+5*paper+1*ink+2*paper
    elif(row == 7):
        return 11*paper
def magnify_letter_n(row,paper,ink):
    '''
    ||||||||||| 11p
    || ||||| || 2p,1i,5p,1i,2p
    ||  |||| || 2p,2i,4p,1i,2p
    || | ||| || 2p,1i,1p,1i,3p,1i,2p
    || ||  | || 2p,1i,2p,2i,1p,1i,2p
    || ||||  || 2p,1i,4p,2i,2p
    ||||||||||| 11p
    '''
    if(row == 1):
        return 11*paper
    elif(row == 2):
        return 2*paper+1*ink+5*paper+1*ink+2*paper
    elif(row == 3):
        return 2*paper+2*ink+4*paper+1*ink+2*paper
    elif(row == 4):
        return 2*paper+1*ink+1*paper+1*ink+3*paper+1*ink+2*paper
    elif(row == 5):
        return 2*paper+1*ink+2*paper+2*ink+1*paper+1*ink+2*paper
    elif(row == 6):
        return 2*paper+1*ink+4*paper+2*ink+2*paper
    elif(row == 7):
        return 11*paper
def magnify_letter_o(row,paper,ink):
    '''
    ||||||||||| 11p
    |||     ||| 3p,5i,3p
    || ||||| || 2p,1i,5p,1i,2p
    || ||||| || 2p,1i,5p,1i,2p
    || ||||| || 2p,1i,5p,1i,2p
    |||     ||| 3p,5i,3p
    ||||||||||| 11p
    '''
    if(row == 1):
        return 11*paper
    elif(row == 2):
        return 3*paper+5*ink+3*paper
    elif(row == 3):
        return 2*paper+1*ink+5*paper+1*ink+2*paper
    elif(row == 4):
        return 2*paper+1*ink+5*paper+1*ink+2*paper
    elif(row == 5):
        return 2*paper+1*ink+5*paper+1*ink+2*paper
    elif(row == 6):
        return 3*paper+5*ink+3*paper
    elif(row == 7):
        return 11*paper
def magnify_letter_p(row,paper,ink):
    '''
    ||||||||||| 11p
    |||     ||| 3p,5i,3p
    ||| |||  || 3p,1i,3p,2i,2p
    |||     ||| 3p,5i,3p
    ||| ||||||| 3p,1i,7p
    ||| ||||||| 3p,1i,7p
    ||||||||||| 11p
    '''
    if(row == 1):
        return 11*paper
    elif(row == 2):
        return 3*paper+5*ink+3*paper
    elif(row == 3):
        return 3*paper+1*ink+3*paper+2*ink+2*paper
    elif(row == 4):
        return 3*paper+5*ink+3*paper
    elif(row == 5):
        return 3*paper+1*ink+7*paper
    elif(row == 6):
        return 3*paper+1*ink+7*paper
    elif(row == 7):
        return 11*paper
def magnify_letter_q(row,paper,ink):
    '''
    ||||||||||| 11p
    ||||    ||| 4p,4i,3p
    ||| |||| || 3p,1i,4p,1i,2p
    ||| |||| || 3p,1i,4p,1i,2p
    ||| || | || 3p,1i,2p,1i,1p,1i,2p
    ||||    ||| 4p,4i,3p
    ||||||||||| 11p
    '''
    if(row == 1):
        return 11*paper
    elif(row == 2):
        return 4*paper+4*ink+3*paper
    elif(row == 3):
        return 3*paper+1*ink+4*paper+1*ink+2*paper
    elif(row == 4):
        return 3*paper+1*ink+4*paper+1*ink+2*paper
    elif(row == 5):
        return 3*paper+1*ink+2*paper+1*ink+1*paper+1*ink+2*paper
    elif(row == 6):
        return 4*paper+4*ink+3*paper
    elif(row == 7):
        return 11*paper
def magnify_letter_r(row,paper,ink):
    '''
    ||||||||||| 11p
    |||     ||| 3p,5i,3p
    ||| |||  || 3p,1i,3p,2i,2p
    |||     ||| 3p,5i,3p
    ||| || |||| 3p,1i,2p,1i,4p
    ||| ||| ||| 3p,1i,3p,1i,3p
    ||||||||||| 11p
    '''
    if(row == 1):
        return 11*paper
    elif(row == 2):
        return 3*paper+5*ink+3*paper
    elif(row == 3):
        return 3*paper+1*ink+3*paper+2*ink+2*paper
    elif(row == 4):
        return 3*paper+5*ink+3*paper
    elif(row == 5):
        return 3*paper+1*ink+2*paper+1*ink+4*paper
    elif(row == 6):
        return 3*paper+1*ink+3*paper+1*ink+3*paper
    elif(row == 7):
        return 11*paper
def magnify_letter_s(row,paper,ink):
    '''
    ||||||||||| 11p
    |||     ||| 3p,5i,3p
    ||  ||||||| 2p,2i,7p
    ||||| ||||| 5p,1i,5p
    |||||||  || 7p,2i,2p
    |||     ||| 3p,5i,3p
    ||||||||||| 11p
    '''
    if(row == 1):
        return 11*paper
    elif(row == 2):
        return 3*paper+5*ink+3*paper
    elif(row == 3):
        return 2*paper+2*ink+7*paper
    elif(row == 4):
        return 5*paper+1*ink+5*paper
    elif(row == 5):
        return 7*paper+2*ink+2*paper
    elif(row == 6):
        return 3*paper+5*ink+3*paper
    elif(row == 7):
        return 11*paper
def magnify_letter_t(row,paper,ink):
    '''
    ||||||||||| 11p
    |||      || 3p,6i,2p
    ||||| ||||| 5p,1i,5p
    ||||| ||||| 5p,1i,5p
    ||||| ||||| 5p,1i,5p
    ||||| ||||| 5p,1i,5p
    ||||||||||| 11p
    '''
    if(row == 1):
        return 11*paper
    elif(row == 2):
        return 3*paper+6*ink+2*paper
    elif(row == 3):
        return 5*paper+1*ink+5*paper
    elif(row == 4):
        return 5*paper+1*ink+5*paper
    elif(row == 5):
        return 5*paper+1*ink+5*paper
    elif(row == 6):
        return 5*paper+1*ink+5*paper
    elif(row == 7):
        return 11*paper
def magnify_letter_u(row,paper,ink):
    '''
    ||||||||||| 11p
    || ||||| || 2p,1i,5p,1i,2p
    || ||||| || 2p,1i,5p,1i,2p
    || ||||| || 2p,1i,5p,1i,2p
    || ||||| || 2p,1i,5p,1i,2p
    |||     ||| 3p,5i,3p
    ||||||||||| 11p
    '''
    if(row == 1):
        return 11*paper
    elif(row == 2):
        return 2*paper+1*ink+5*paper+1*ink+2*paper
    elif(row == 3):
        return 2*paper+1*ink+5*paper+1*ink+2*paper
    elif(row == 4):
        return 2*paper+1*ink+5*paper+1*ink+2*paper
    elif(row == 5):
        return 2*paper+1*ink+5*paper+1*ink+2*paper
    elif(row == 6):
        return 3*paper+5*ink+3*paper
    elif(row == 7):
        return 11*paper
def magnify_letter_v(row,paper,ink):
    '''
    ||||||||||| 11p
    || ||||| || 2p,1i,5p,1i,2p
    || ||||| || 2p,1i,5p,1i,2p
    ||| ||| ||| 3p,1i,3p,1i,3p
    ||||   |||| 4p,3i,4p
    ||||| ||||| 5p,1i,5p
    ||||||||||| 11p
    '''
    if(row == 1):
        return 11*paper
    elif(row == 2):
        return 2*paper+1*ink+5*paper+1*ink+2*paper
    elif(row == 3):
        return 2*paper+1*ink+5*paper+1*ink+2*paper
    elif(row == 4):
        return 3*paper+1*ink+3*paper+1*ink+3*paper
    elif(row == 5):
        return 4*paper+3*ink+4*paper
    elif(row == 6):
        return 5*paper+1*ink+5*paper
    elif(row == 7):
        return 11*paper
def magnify_letter_w(row,paper,ink):
    '''
    ||||||||||| 11p
    || ||||| || 2p,1i,5p,1i,2p
    || ||||| || 2p,1i,5p,1i,2p
    || || || || 2p,1i,2p,1i,2p,1i,2p
    || | | | || 2p,1i,1p,1i,1p,1i,1p,1i,2p
    || ||||| || 2p,1i,5p,1i,2p
    ||||||||||| 11p
    '''
    if(row == 1):
        return 11*paper
    elif(row == 2):
        return 2*paper+1*ink+5*paper+1*ink+2*paper
    elif(row == 3):
        return 2*paper+1*ink+5*paper+1*ink+2*paper
    elif(row == 4):
        return 2*paper+1*ink+2*paper+1*ink+2*paper+1*ink+2*paper
    elif(row == 5):
        return 2*paper+1*ink+1*paper+1*ink+1*paper+1*ink+1*paper+1*ink+2*paper
    elif(row == 6):
        return 2*paper+1*ink+5*paper+1*ink+2*paper
    elif(row == 7):
        return 11*paper
def magnify_letter_x(row,paper,ink):
    '''
    ||||||||||| 11p
    || ||||| || 2p,1i,5p,1i,2p
    ||| ||| ||| 3p,1i,3p,1i,3p
    ||||| ||||| 5p,1i,5p
    ||| ||| ||| 3p,1i,3p,1i,3p
    || ||||| || 2p,1i,5p,1i,2p
    ||||||||||| 11p
    '''
    if(row == 1):
        return 11*paper
    elif(row == 2):
        return 2*paper+1*ink+5*paper+1*ink+2*paper
    elif(row == 3):
        return 3*paper+1*ink+3*paper+1*ink+3*paper
    elif(row == 4):
        return 5*paper+1*ink+5*paper
    elif(row == 5):
        return 3*paper+1*ink+3*paper+1*ink+3*paper
    elif(row == 6):
        return 2*paper+1*ink+5*paper+1*ink+2*paper
    elif(row == 7):
        return 11*paper
def magnify_letter_y(row,paper,ink):
    '''
    ||||||||||| 11p
    || ||||| || 2p,1i,5p,1i,2p
    ||| ||| ||| 3p,1i,3p,1i,3p
    ||||| ||||| 5p,1i,5p
    ||||| ||||| 5p,1i,5p
    ||||| ||||| 5p,1i,5p
    ||||||||||| 11p
    '''
    if(row == 1):
        return 11*paper
    elif(row == 2):
        return 2*paper+1*ink+5*paper+1*ink+2*paper
    elif(row == 3):
        return 3*paper+1*ink+3*paper+1*ink+3*paper
    elif(row == 4):
        return 5*paper+1*ink+5*paper
    elif(row == 5):
        return 5*paper+1*ink+5*paper
    elif(row == 6):
        return 5*paper+1*ink+5*paper
    elif(row == 7):
        return 11*paper
def magnify_letter_z(row,paper,ink):
    '''
    ||||||||||| 11p
    ||       || 2p,7i,2p
    ||||||  ||| 6p,2i,3p
    ||||   |||| 4p,3i,4p
    |||  |||||| 3p,2i,6p
    ||       || 2p,7i,2p
    ||||||||||| 11p
    '''
    if(row == 1):
        return 11*paper
    elif(row == 2):
        return 2*paper+7*ink+2*paper
    elif(row == 3):
        return 6*paper+2*ink+3*paper
    elif(row == 4):
        return 4*paper+3*ink+4*paper
    elif(row == 5):
        return 3*paper+2*ink+6*paper
    elif(row == 6):
        return 2*paper+7*ink+2*paper
    elif(row == 7):
        return 11*paper
def magnify_letter_unknown(row,paper,ink):
    '''
    ||||||||||| 11p
    ||||||||||| 11p
    ||||||||||| 11p
    ||||||||||| 11p
    ||||||||||| 11p
    ||       || 11p
    ||||||||||| 11p
    '''
    if(row == 1):
        return 11*paper
    elif(row == 2):
        return 11*paper
    elif(row == 3):
        return 11*paper
    elif(row == 4):
        return 11*paper
    elif(row == 5):
        return 11*paper
    elif(row == 6):
        return 2*paper+7*ink+2*paper
    elif(row == 7):
        return 11*paper
