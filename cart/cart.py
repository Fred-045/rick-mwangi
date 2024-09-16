from store.models import Product


class Cart():
  def __init__(self, request):
    self.session = request.session
    
    # Get the current seesion key if it exist
    cart = self.session.get('session_key')
    
    #if the user is new no session key
    if 'session_key' not in request.session:
      cart = self.session['session_key'] = {}
      
#MAKE SURE THAT CART IS AVAILABLE TO ALL PAGES OF SITE
    self.cart = cart 
    
  def add(self, product, quantity):
    product_id = str(product.id)
    product_qty = str(quantity)
  #LOGIC
    if product_id in self.cart:
      pass
    
    else:
      #self.cart[product_id] = {'price': str(product.price)}
      self.cart[product_id] = int(product_qty)
    self.session.modified = True
    
  def __len__(self):
    return len(self.cart)
  
  def get_prods(self):
    products_ids = self.cart.keys()
    
    #USE IDs TO LOOK UP PRODUCTS IN THE DATABASE MODELS
    products = Product.objects.filter(id__in=products_ids)
    #return those looked up products
    return products
  
  def get_quants(self):
    quantities = self.cart
    return quantities
      