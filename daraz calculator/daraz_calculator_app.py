from flask import Flask,render_template,request
app=Flask(__name__)
@app.route("/")
def daraz_calculator():
    return render_template("calclator.html")

    
 
@app.route('/result',methods=['GET','POST'])
def result():
        
        dsp=int(request.form["daraz_selling_price"])
        dcp=int(request.form["daraz_cost_price"])
        commission=int(request.form["Commisssion"])
        shipfee=int(request.form["shipping"])
        fp_expenses=int(request.form["fp_expenses"])
        cm=commission/100
        com=dsp*cm
        shipcharges=dsp*0.04
        payment_fee=dsp*0.05
        gtotal=dsp-shipfee-fp_expenses-com-shipcharges-payment_fee
        if dcp<gtotal:
            p="profit"
            n=gtotal-dcp
        elif dcp==gtotal:
            p="not profit cost price and grand total are same"
            n=gtotal-dcp
        else:
            p="loss"
            n=gtotal-dcp 
                     
        return render_template("result.html",dsp=dsp,dcp=dcp,com=com,shipfee=shipfee,fp_expenses=fp_expenses,shipcharges=shipcharges,payment_fee=payment_fee,gtotal=gtotal,p=p,n=n)   
    
app.run(debug=True,port=8000) 


