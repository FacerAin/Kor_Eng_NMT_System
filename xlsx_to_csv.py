import pandas as pd
def xlsx_to_csv(org_filename, src_filename, org_path, src_path, org_attr, src_attr):
    data_xlsx_org = pd.read_excel(org_path+filename,org_attr, index_col=None, header=None)
    data_xlsx_src = pd.read_excel(org_path+filename,src_attr, index_col=None, header=None)
    data_xlsx_org.to_csv(src_path+src_filename, encoding='utf-8', index = False)
    data_xlsx_src.to_csv(src_path+src_filename, encoding='utf-8', index = False)

