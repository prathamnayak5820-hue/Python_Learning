with open("hello.txt","r") as file:
        h=0
        t= " "
    
        l = file.readlines()
        
        for i in l:
            q = i.split()
            name = q[0]
            marks =int(q[1])
            if marks>0:
                  h=marks
                  t = name

            
       
        print(t,h)
            

        
           
        
  


    