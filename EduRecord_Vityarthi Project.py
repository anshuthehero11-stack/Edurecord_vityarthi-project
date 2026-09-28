class pr:
    def mk1(self,i,n):
        self.i=i
        self.n=n
class st(pr):
    def mk2(self,i,n):
        self.mk1(i,n)
        self.cs=set()
        self.gs={}
    def ad(self,c):
        if c in self.cs:
            print("already enrolled")
            return 0
        self.cs.add(c)
        return 1
    def gr(self,c,g):
        if c not in self.cs:
            print("not enrolled in course")
            return 0
        self.gs[c]=g
        return 1
d={}
r=1
while r==1:
    print("menu options")
    print("1 add student")
    print("2 enroll course")
    print("3 add grade")
    print("4 show failed students")
    print("5 search student by id")
    print("6 exit")
    c=input("type 1 2 3 4 5 or 6 ")
    if c=='1':
        i=input("student id ")
        n=input("student name ")
        o=st()
        o.mk2(i,n)
        d[i]=o
        print("student added")
    elif c=='2':
        i=input("student id ")
        if i in d:
            x=input("course name ")
            s=d[i].ad(x)
            if s==1:
                print("course enrolled")
        else:
            print("no student found")
    elif c=='3':
        i=input("student id ")
        if i in d:
            x=input("course name ")
            g=float(input("grade "))
            s=d[i].gr(x,g)
            if s==1:
                print("grade saved")
        else:
            print("no student found")
    elif c=='4':
        f=0
        for k in d:
            for x in d[k].gs:
                if d[k].gs[x]<50:
                    print("student",d[k].n,"failed",x,"with",d[k].gs[x])
                    f=1
        if f==0:
            print("no failed students")
    elif c=='5':
        i=input("student id to search ")
        if i in d:
            print("name",d[i].n)
            if len(d[i].cs)==0:
                print("no courses")
            for x in d[i].cs:
                if x in d[i].gs:
                    print("course",x,"grade",d[i].gs[x])
                else:
                    print("course",x,"no grade")
        else:
            print("no student found")
    elif c=='6':
        r=0
    else:
        print("wrong input try again")