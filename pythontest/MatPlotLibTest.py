import matplotlib.pyplot as plt
input_value=[1,2,3,4,5]
squares=[1,4,9,16,25]
plt.plot(input_value,squares,linewidth=5)
plt.title("Square Numbers",fontsize=18)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of value",fontsize=14)
plt.tick_params(axis='both',labelsize=14)
plt.show()

x_values=[1,2,3,4,5]
y_values=[1,4,9,16,25]
plt.scatter(x_values,y_values,s=100)
plt.title("Square Numbers",fontsize=24)
plt.xlabel("value",fontsize=14)
plt.ylabel("Square of value",fontsize=14)
plt.tick_params(axis='both',which='major',labelsize=14)
plt.show()


#自动计算数据
x_value=list(range(1,1001))
y_value=[x**2 for x in x_value]
plt.scatter(x_value,y_value,edgecolors='none',s=40)
plt.axis([0,1100,0,1100000])     #设置每个坐标轴的取值范围
plt.show()


#自动计算数据
x_value=list(range(1,1001))
y_value=[x**2 for x in x_value]
plt.scatter(x_value,y_value,c='red',edgecolors='none',s=40)
plt.axis([0,1100,0,1100000])     #设置每个坐标轴的取值范围
plt.show()


#自动计算数据
x_value=list(range(1,1001))
y_value=[x**2 for x in x_value]
plt.scatter(x_value,y_value,c=y_value,cmap=plt.cm.Blues,edgecolors='none',s=40)
plt.axis([0,1100,0,1100000])     #设置每个坐标轴的取值范围
plt.show()
