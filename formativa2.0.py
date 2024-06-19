agregar_trabajadores=[]
des_seguVida=0.07
desc_AFP=0.12
def agregar_trabajadores_func():
                        
                        trabajador=input("ingrese el nombre y a epellido del empleado : ")
                        print("-" *20)
                        print("una vez ingresado el nombre, ingrese el puesto del empleado")
                        print("1.- CEO")
                        print("2.- DESARROLLADOR")
                        print("3.- ANALISTA PROGRAMADOR")
                        cargo=int(input(": "))
                        if cargo ==1:
                                cargo="CEO"

                        elif cargo ==2:
                                cargo= "DESARROLLADOR"  

                        elif cargo==3:
                                cargo= "ANALISTA PROGRAMADOR" 
                                print("-" *20)  
                                
                        sueldo=int(input("ingrese el sueldo del trabajador : "))
                        sueldo_liquido=(sueldo-(sueldo*0.07+ sueldo*0.12))
                        
                        
                        agregar_trabajadores.append([trabajador, cargo, sueldo, sueldo_liquido])
                       

opc=-1
encabezado=["nombre", "cargo"," sueldo_bruto", " sueldo_liquido"]






while opc!=-4:
        print("bienvenido al programa de trabajadores ")
        print("menu")
        print(f"-"*50)
        print("1.- reguistrar_trabajador ")
        print("2.- listar todos los trabajadores ")
        print("3.- imprimir sueldos ")
        print("4.- salir del programa ")
        print("-"*20)
        opc=int(input("ingrese una opcion : "))
        match opc:
                case 1:
                       agregar_trabajadores_func()

                       



                case 2:
                        print(encabezado)
                        for trabajador in agregar_trabajadores:
                                print(trabajador)
                
                

                case 3: 
                        with open("archivo.txt", "w") as archivo:
                                for trabajador in agregar_trabajadores:
                                         archivo.write(", ".join(map(str, trabajador)) + "\n")

                case 4:
                        print("hasta la proxima, gracias por esatr con nosotros")









                      



  
   