from config import app
from blueprints.users.views import bp_users
from blueprints.orders.views import bp_orders
from blueprints.offers.views import bp_offers
from functions import Functions

app.register_blueprint(bp_users, url_prefix='/users')
app.register_blueprint(bp_orders, url_prefix='/orders')
app.register_blueprint(bp_offers, url_prefix='/offers')
func = Functions()

if __name__ == "__main__":
    func.init_base()
    app.run(debug=True)
