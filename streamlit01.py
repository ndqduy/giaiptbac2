import streamlit as st 
import math


st.title("GIAI PHUONG TRINH BAC 2")



# Introduction

st.subheader("Introduction")

st.text("""
PT BAC 1: A = 0
B=0, C#0 => PT VO N

B=0, C=0 => PT VO SO N

B#0, C#0 => X=-C/B

PT BAC 2: A#0
delta = B**2-4*A*C
    DELTA <0 => PT VO N
    DELTA =0 => X=-B/2A
    DELTA >0 => x1=(-b+math.sqrt(delta))/(2*a)
                x2=(-b-math.sqrt(delta))/(2*a)
        

	""")


# Input

A = st.number_input("Enter A VALUE", step=0.1)

B = st.number_input("Enter B VALUE", step=0.1)

C = st.number_input("Enter C VALUE", step=0.1)

if A==0:   #pt bậc 1
        if B ==0  and C !=0:
            e = st.write("pt vo n")
        elif B==0 and C ==0:
            e = st.write("pt vo so n")
        else:
            x = -C/B
            e= str(x)

elif A !=0: #pt bac 2 
        delta = B**2-4*A*C
        if delta < 0:
            e = st.write("pt vo n")
        elif delta ==0:
            x = -B/2*A
            e =  str(x)
        else:
            x1=(-B+math.sqrt(delta))/(2*A)
            x2=(-B-math.sqrt(delta))/(2*A)
            e =  str(x1) + " and "+ str(x2)


st.success(f" KET QUA {e}")