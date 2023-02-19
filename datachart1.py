import numpy as np
import matplotlib.pyplot as plt
# x=np.linspace(0,4*np.pi,800)
# y=np.sin(x)
# ax=plt.subplot()
# ax.plot(x,y)
#
# plt.show()

# Todo:second
# x=np.random.uniform(0,1,100)
# y=np.random.uniform(0,1,100)
# plt.scatter(x,y)
# plt.show()
#Todo:third

# x=np.arange(10)
# y=np.random.uniform(1,10,10)
# plt.bar(x,y)
# plt.show()
# Todo:routh
# z=np.random.normal(1,1,100)
# x=np.arange(5)
# y=np.random.uniform(0,1,5)
# z=np.random.normal(10,100,(100,9))
# plt.imshow(z)
# ax=plt.subplot()
# ax.contourf(z)
# ax.pie(z)
# ax.errorbar(x,y,y/4)
# ax.hist(z)
# ax.boxplot(z)
# plt.show()

# Todo:Tweak
x=np.linspace(0,10,100)
y=np.sin(x)
# ax=plt.subplot()
# plt.title('Chart')
# plt.plot(x,y,color='green')
# ax.plot(x,y,linestyle="--")
# ax.plot(x,y,linewidth=5)
# ax.plot(x,y,marker="o")
# plt.grid()
# fig,(a,a2)=plt.subplots(2,1)
y1,y2=np.sin(x),np.cos(x)
# # plt.plot(x,y1,x,y2)
# a.plot(x,y1,color="red")
# a2.plot(x,y2,'g')
#
# plt.show()
#Todo:organize

fig,(a,a2)=plt.subplots(1,2)
fig.suptitle('none')
plt.title('a sine wave')
plt.xlabel('time')
plt.ylabel('upper')
a.plot(y1,x,'+')

a2.plot(y2,x,':')
fig.savefig('my-first.png',dpi=300)

plt.show()

# todo:label
# plt.plot(x,y)
# plt.suptitle('vh')
# plt.set_title('hvj')