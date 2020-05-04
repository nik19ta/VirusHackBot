from virushack_corona import predict_corona


test = [[1, 10, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1,0,1,0,1,1,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,1]]

# print('Вероятность того, что вы зараженны короновирусом '  + str(predict_corona(test) * 100)[1] + str(predict_corona(test) * 100)[2] + ' %')


def getdata():
    p = predict_corona(test)

    if int(str(p * 100)[1] + str(p * 100)[2]) > 0  :
        return str('Вероятность того, что вы зараженны короновирусом '  + str(p * 100)[1] + str(p * 100)[2] + ' %')
    else:
        return str('Вероятность того того что вы больны очень мала')

print(getdata())
