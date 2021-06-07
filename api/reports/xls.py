# coding=utf-8
from django.http import HttpResponse
from datetime import datetime
import xlsxwriter
from decimal import Decimal
import io



def generateXls(report_name='reporte',data=[], *args, **kwargs):
    try:
        output = io.BytesIO()

        if 'hour_start' in kwargs:
            hour_start = kwargs['hour_start']
        else:
            hour_start = None

        if 'hour_end' in kwargs:
            hour_end = kwargs['hour_end']
        else:
            hour_end = None

        if 'header_keys' in kwargs:
            header_keys = kwargs['header_keys']
        else:
            header_keys = None

        if 'totalizator' in kwargs:
            totalizator = kwargs['totalizator']
        else:
            totalizator = True
    
        
        workbook = xlsxwriter.Workbook(output, {'in_memory': True})
        worksheet = workbook.add_worksheet(report_name)

        format_bold = workbook.add_format({
        'bold': 1,
        'align': 'left',
        'valign': 'vcenter',
        'text_wrap':'false'})

        format_regular = workbook.add_format({
        'bold': 0,
        'align': 'right',
        'valign': 'vcenter',
        'text_wrap':'false'})

        number_format_bold = workbook.add_format({
            'bold': 1,
            'num_format': '[$$-409]#,##0.00'})

        number_format = workbook.add_format({
            'num_format': '[$$-409]#,##0.00'})     

        format_bold.set_shrink()
        format_regular.set_shrink()
        number_format.set_shrink()
        number_format_bold.set_shrink()
        
       
        row = 1
        row2 = 0
        i = 0
        
        for key in header_keys:
            ele =  list(key.keys())
            worksheet.set_column(row2, i, 20)
            worksheet.write(row2,i, str(ele[0]),format_bold)
            i=i+1

        length = len(data)
        pos = 0
        total = [] 

        for iterator in header_keys:
            total.append(0)
            if length == 0:
                total.append(0)
        
        for i in data:
            col = 0
            for j in i:
                ele = list(header_keys[col].values())
                if ele[0] == 'int':
                    total[col] = int(total[col]) + int(i[j])
                    worksheet.write(row,col, str(i[j]), format_regular)
                elif ele[0] == 'float':
                    total[col] = Decimal(total[col] + i[j])
                    worksheet.write(row,col,i[j], number_format)

                elif ele[0] == 'porc':
                    total[col] = Decimal(total[col] + i[j])
                    worksheet.write(row,col, str("{}%".format(i[j]) ), format_regular)
                else:
                    worksheet.write(row,col, str(i[j]), format_regular)
                col = col + 1
                
            row += 1
            pos += 1
        
        workbook.close()

        output.seek(0)

        response = HttpResponse(output.read(),
                                content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
        response['Content-Disposition'] = "attachment; filename={}.xlsx".format(report_name)

        output.close()

        return response
    except Exception as e:
        data = {'message': str(e), 'code': 2, 'data': None}
        print(data)