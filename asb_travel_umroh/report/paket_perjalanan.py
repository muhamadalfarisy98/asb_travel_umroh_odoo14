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
        # if '-' not in data:
        #     data=objects.get_report_student_class_data()
        ws.merge_range(0,0,0,2,'Daftar Manifest Jamaah ',style['title'])
        ws.merge_range(1,0,1,2,objects.name,style['title'])
        # row=6
        # table1 =(
        #                 ['No', 12],
        #                 ['STUDENT ID', 20],
        #                 ['NAMA', 20],
        # )
        # for l in data:
        #     ws.write(row-4,0,'Kelas',style['blue_center'])
        #     ws.write(row+1-4,0,self.get_nama_kelas(l[1],l[0]))
        #     ws.merge_range(row-4,1,row-4,2,'Wali Kelas',style['blue_center'])
        #     ws.merge_range(row+1-4,1,row+1-4,2,l[2])
        #     col=0
        #     for item,size in table1:
        #         ws.set_column(col,col,size)
        #         ws.write(row-1,col,item,style['yellow_center'])
        #         col+=1
        #     num=1
        #     for student in l[5]:
        #         ws.write(row,0,num)
        #         ws.write(row,1,student.student_code)
        #         ws.write(row,2,student.student_name)
        #         num+=1
        #         row+=1
        #     row+=6

    # def get_nama_kelas(self,jenjang,nama):
    #     return '[ '+jenjang+' ] '+nama