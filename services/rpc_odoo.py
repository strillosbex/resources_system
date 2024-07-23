# -*- coding: utf-8 -*-
import xmlrpc.client

class rpc_wms:
    
    def __init__(self, url_rpc, db_rpc, username_rpc, password_rpc):
        self.url_rpc = url_rpc
        self.db_rpc = db_rpc
        self.username_rpc = username_rpc
        self.password_rpc = password_rpc
        self.models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url_rpc))
    
    def connection_odoo(self):
        try:
            common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(self.url_rpc))
            uid = common.authenticate(self.db_rpc, self.username_rpc, self.password_rpc, {})
            return True, uid
        except Exception as err:
            return False, err
    
    def search_read_odoo(self, uid, model, filters, fields, limit=0):
        try:
            result = self.models.execute_kw(self.db_rpc, uid, self.password_rpc,
                model, 'search_read',
                [
                    filters
                ],
                {
                    'fields': fields,
                    'limit': limit
                }
                
            )
            return True, result
        except Exception as err:
            return False, err
    
    def search_odoo(self, uid, model, filters, limit=0):
        try:
            result = self.models.execute_kw(self.db_rpc, uid, self.password_rpc,
                model, 'search',
                [
                    filters
                ],
                {
                    'limit': limit
                }
                
            )
            return True, result
        except Exception as err:
            return False, err
    
    def search_count_odoo(self, uid, model, filters):
        try:
            result = self.models.execute_kw(self.db_rpc, uid, self.password_rpc, 
                model, 'search_count', 
                [
                    filters
                ]
            )        
            return True, result
        except Exception as err:
            return False, err
    
    def create_odoo(self, uid, model, fields):
        try:
            result = self.models.execute_kw(self.db_rpc, uid, self.password_rpc,
                model, 'create',
                [
                    fields
                ]
            )
            return True, result
        except xmlrpc.client.Fault as err:
            return False, err.faultString
    
    def write_odoo(self, uid, model, code, fields):
        try:
            result = self.models.execute_kw(self.db_rpc, uid, self.password_rpc, 
                model, 'write',
                [
                    [code],
                    fields
                ]
            )
            return True, result
        except xmlrpc.client.Fault as err:
            return False, err.faultString
    
    def unlink_odoo(self, uid, model, code):
        try:
            result = self.models.execute_kw(self.db_rpc, uid, self.password_rpc, 
                model, 'unlink',
                [
                    [code]
                ]
            )
            return True, result
        except xmlrpc.client.Fault as err:
            return False, err.faultString