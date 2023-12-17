# VendorManagementSystem


## setup 
git clone https://github.com/chandru-shane/VendorManagementSystem.git
cd VendorManagementSystem
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt


## testing
pytest .

## run http server
python src/manage.py migrate
python src/manage.py runserver

## API Documentation

### Vendor api
POST /api/vendors/ -> To create vendor
GET /api/vendors/ -> To list all vendors
 
GET /api/vendors/{vendor_id}/ -> To retrive the particular vendor with vendor id
PUT /api/vendors/{vendor_id}/ -> Update a vendor's details with vendor id
DELETE /api/vendors/{vendor_id}/ -> To delete the vendor

### Purchase api
POST /api/purchase_orders/ ->  Create a purchase order
GET /api/purchase_orders/ -> List all purchase orders with an option to filter by vendor id
PUT /api/purchase_orders/{po_id}/ -> Update a purchase order
DELETE /api/purchase_orders/{po_id} -> Delete a purchase order

### Performance Analytics
GET /api/vendors/{vendor_id}/performance -> Retrieve a vendor's performance metrics.
