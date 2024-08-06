import matplotlib.pyplot as plt
idades=[65,26,67,50,47,73,1,58,2,94,12,22,12,95,25,13,61,41,24,95,
        3,71,53,24,23,44,83,30,19,32,71,66,45,6,99,4,76,27,50,18,58,                 61,53,72,14,78,36,89,6,71,58,69,22,34,38,51,71,83,22,22,36,44,        16,58,20,49,28,55,21,26,23,41,21,95,18,63,55,2,61,81,39,20,39,
17,66,60,73,26,54,16,76,83,9,12,15,35,54,11,7,61]
plt.title('Idades de um grupo', fontsize=20)
plt.xlabel('Idade', fontsize=15)
plt.ylabel('Frequência Absoluta', fontsize=15)
plt.tick_params(labelsize=15)
plt.hist(idades, 5, rwidth=0.9, color='red', alpha=0.7, edgecolor='black')
plt.show()