# VendorManagementSystem


## setup <br/>
git clone https://github.com/chandru-shane/VendorManagementSystem.git<br/>
cd VendorManagementSystem<br/>
python3 -m venv venv<br/>
source venv/bin/activate<br/>
pip install -r requirements.txt<br/>


## testing<br/>
cd src
export DJANGO_SETTINGS_MODULE=backend.settings
pytest .<br/>

## run http server<br/>
python src/manage.py migrate<br/>
python src/manage.py runserver<br/>

## API Documentation<br/>

### Vendor api<br/>
POST /api/vendors/ -> To create vendor<br/>
GET /api/vendors/ -> To list all vendors<br/>
 
GET /api/vendors/{vendor_id}/ -> To retrive the particular vendor with vendor id<br/>
PUT /api/vendors/{vendor_id}/ -> Update a vendor's details with vendor id<br/>
DELETE /api/vendors/{vendor_id}/ -> To delete the vendor<br/>

### Purchase api<br/>
POST /api/purchase_orders/ ->  Create a purchase order<br/>
GET /api/purchase_orders/ -> List all purchase orders with an option to filter by vendor id<br/>
PUT /api/purchase_orders/{po_id}/ -> Update a purchase order<br/>
DELETE /api/purchase_orders/{po_id} -> Delete a purchase order<br/>

### Performance Analytics<br/>
GET /api/vendors/{vendor_id}/performance -> Retrieve a vendor's performance metrics.<br/>
