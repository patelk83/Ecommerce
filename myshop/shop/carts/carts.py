from flask import  redirect,render_template,url_for,flash,request,session,current_app
from shop import db, app
from shop.products.models import Addproduct

def MAgerDicts(dict1, dict2):
    if isinstance(dict1,list) and isinstance(dict2,list):
        return dict1 + dict2
    elif isinstance(dict1, dict) and isinstance(dict2,dict):
        return False

@app.route('/addcart',methods=['POST'])
def AddCart():
    try:
        product_id = request.form.get('product_id')
        quantity = request.form.get('quantity')
        colors= request.form.get('colors')
        product= Addproduct.query.filter_by(id=product_id).first()
        if product_id and quantity and colors and request.method =="POST":
            DictItems ={ product_id:{'name':product.name, 'price':product.price,'discount':product.discount,
                                     'color':colors, 'quantity':quantity, 'image':product.image_1}}
            if 'Shoppingcart' in session:
                print(session('Shoppingcart'))
                if product_id in session['Shoppingcart']:
                    print("This product already in cart")
                else:
                    session['Shoppingcart']= MAgerDicts(session['Shoppingcart'],DictItems)
                    return redirect(request.referrer)
            else:
                session['Shoppingcart'] = DictItems
                return redirect(request.referrer)
    except Exception as e:
        print(e)
    finally:
        return redirect(request.referrer)

@app.route('/carts')
def getCart():
    if 'Shoppingcart' not in session:
        return redirect(request.referrer)
    subtotal=0
    grandtotal=0
    for key,product in session['Shoppingcart'].items():
        discount=(product['discount']/100) * float(product['price'])
        subtotal += float(product['price']) * int(product['quantity'])
        subtotal -= discount
        tax= ("%.2f" % (0.06 * float(subtotal)))
        grandtotal= float("%.2f" % (1.06 * subtotal))
    return render_template('products.carts.html', tax=tax, grandtotal=grandtotal)
