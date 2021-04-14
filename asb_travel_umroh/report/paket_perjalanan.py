from odoo import models
from xlsxwriter.utility import xl_rowcol_to_cell
from datetime import datetime

class ReportAccountPaymentPlan(models.AbstractModel):
    _name = 'report.asb_travel_umroh.paket_perjalanan'
    _inherit = 'report.report_xlsx.abstract'
    _description = 'XLSX Manifest Jamaah'

    def generate_xlsx_report(self, wb, data, objects, style):
        ws = wb.add_worksheet('Daftar Manifest Jamah')
        #header
        data_manifest=objects.get_report_manifest_jamaah_data()
        data_airlines=objects.get_report_airlines_data()

        ws.write(1,2,'MANIFEST',style['normal_bold_center'])
        ws.write(1,3,objects.name,style['normal_bold_center'])
        row=4
        table1 =(
                        ['No', 12],
                        ['Gender', 15],
                        ['TITLE', 16],
                        ['FULL NAME', 20],
                        ['TEMPAT LAHIR', 20],
                        ['TANGGAL LAHIR', 24],
                        ['NO PASSPORT', 20],
                        ['PASSPORT ISSUED', 20],
                        ['PASSPORT EXPIRED', 20],
                        ['IMIGRASI', 20],
                        ['MAHRAM', 20],
                        ['USIA', 12],
                        ['NIK', 25],
                        ['ORDER', 20],
                        ['ROOM TYPE', 20],
                        ['ALAMAT', 20],
        )
        col=0
        for item,size in table1:
            ws.set_column(col,col,size)
            ws.write(row-1,col,item,style['blue_center'])
            col+=1
        for l in data_manifest:
            ws.write(row,0,l[0])
            ws.write(row,1,l[1])
            ws.write(row,2,l[2])
            ws.write(row,3,l[3])
            ws.write(row,4,l[4])
            ws.write(row,5,l[5].strftime('%d %b %Y'))
            ws.write(row,6,l[6])
            ws.write(row,7,l[7].strftime('%d %b %Y'))
            ws.write(row,8,l[8].strftime('%d %b %Y')) 
            ws.write(row,9,l[9])
            ws.write(row,10,self.get_mahram(objects,l[10]))
            ws.write(row,11,l[11])
            ws.write(row,12,l[12])
            ws.write(row,13,self.get_so_jamaah(objects))
            ws.write(row,14,l[13])
            ws.write(row,15,l[14])
            row+=1

        table2 =(
                        ['No', 12],
                        ['AIRLINES', 15],
                        ['DEPARTURE DATE', 16],
                        ['DEPARTURE CITY', 20],
                        ['ARRIVAL CITY', 24],
        )
        col=2
        row+=3
        for item,size in table2:
            ws.set_column(col,col,size)
            ws.write(row-1,col,item,style['blue_center'])
            col+=1
        for l in data_airlines:
            ws.write(row,2,l[0])
            ws.write(row,3,l[1])
            ws.write(row,4,l[2].strftime('%d %b %Y'))
            ws.write(row,5,l[3])
            ws.write(row,6,l[4])
            row+=1

    def get_so_jamaah(self,objects):
        so_id=self.env['sale.order'].sudo().search([
            ('paket_perjalanan_id','=',objects.id),
        ],limit=1)
        return so_id.name
    
    def get_mahram(self,objects,ids):
        return ', '.join([x.name for x in ids])