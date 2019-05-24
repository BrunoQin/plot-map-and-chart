import matplotlib.pyplot as plt


# num = [0.08418887, -0.01703213, 0.06280119, 0.3071936, 0.1990288, -0.003986935,
#        -0.0585378, -0.2813296, -0.5252239, -1.005211, -1.468974, -1.702035] # JUL

# num = [-0.02160083, -0.03334586, -0.1377528, -0.1022559, -0.1348303, -0.0009527369,
#        -0.06864743, -0.3197093, -0.3766608, -0.2984339, -0.2501658, -0.3465925] # OCT

num = [-0.01121282, 0.03523616, 0.09443916, 0.00671054, -0.06074205, -0.215481,
       -0.4365711, -0.5202628, -0.4541457, -0.3862911, -0.1486375, -0.1834874] # APR

# num = [0.05912766, -0.02680236, -0.02457552, -0.2019524, -0.2639855, -0.1947891,
#        -0.3365076, -0.7386874, -0.9088315, -1.059714, -1.326119, -1.355645] # JAN

ave = []
for i in range(4):
    tem = (abs(num[i*3]) + abs(num[i*3+1]) + abs(num[i*3+2])) / 3
    # tem = (num[i*3] + num[i*3+1] + num[i*3+2]) / 3
    ave.append(tem)

name_list = ['AMJ', 'JAS', 'OND', 'JFM']
plt.bar(range(len(ave)), ave, color='rgb', tick_label=name_list)
plt.show()