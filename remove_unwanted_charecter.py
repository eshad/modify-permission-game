
with open(r'details.txt', 'r') as infile, open(r'details_refactored.txt', 'w') as outfile:
     data = infile.read()
     data = data.replace("\\n", "")
     data = data.replace("[],", "")
     data = data.replace("u'", "")
     data = data.replace("\\t", "")
     # data = data.replace("\\t", "")
     data = data.replace("\\\\\\t", "") # for / use //
     data = data.replace("\\\\\\", "") # for / use //
     data = data.replace("\\\\", "") # for / use //
     data = data.replace("\\", "") # for / use //
     data = data.replace('["[     ', "") # for / use //
     data = data.replace('[Home            Member List             Advanced Search                                     ', "") # for / use //
     data = data.replace(' Company Details           Print Download Member Form                      Primary', "") # for / use //
     data = data.replace(' Information                                  ', "") # for / use //
     data = data.replace('Company Name :           ', "Company Name : ") # for / use //
     data = data.replace('                                  BKMEA Membership', "\nBKMEA Membership : ") # for / use //
     data = data.replace(":'", ": ")
     data = data.replace("Number :            ", "Number :")
     data = data.replace("Membership Type :           ", "Membership Type :")
     data = data.replace("']", "")
     data = data.replace("Machine :                                                                      ", "Machine: ")
     data = data.replace("Member                                  Year of Registration :           ", "Member:\nYear of Registration :")
     data = data.replace("Home            Member List             Advanced Search', Home', Member List', Advanced Search',", "")
     data = data.replace("Contact Person Designation :", "\nContact Person Designation :")
     data = data.replace("Contact Person Designation :            ", "Contact Person Designation : ")
     data = data.replace("Addresses :            ", "Addresses : ")
     data = data.replace("Addresses :", "\nAddresses : ")
     data = data.replace("ContactContact Person Name :", "\nContactContact Person Name :")
     data = data.replace("Contact Person Mobile Number :", "\nContact Person Mobile Number :")
     data = data.replace("Telephone :", "\nTelephone :")
     data = data.replace("Fax :", "\nFax :")
     data = data.replace("OfficeAddress :", "\nOfficeAddress : ")
     data = data.replace("Email :", "\nEmail :")
     data = data.replace("Web :                                                            ", "\nWeb : ")
     data = data.replace("FactoryFactory Category :             ", "\nFactory Category : ")
     data = data.replace("                                Number of Machine:", "\nNumber of Machine: ")
     data = data.replace("   Production Capacity :", "\nProduction Capacity :")
     data = data.replace("   Production Capacity :", "\nProduction Capacity :")
     data = data.replace("                                   Number of Employee (Workers) :", "\nNumber of Employee (Workers) : ")
     data = data.replace("                                            Yearly Turnover (In US$) :            0                                 ", "\nYearly Turnover (In US$) :0")
     data = data.replace("Back to Member List', ", "\nBack to Member List-->")
     data = data.replace("                                  Membership Type", "\nMembership Type")
     data = data.replace(" Company Name :", "\nCompany Name :")
     data = data.replace("BKMEA Membership :  Number :", "BKMEA Membership Number : ")
     data = data.replace("                                            Yearly Turnover (In US$) :", "\nYearly Turnover (In US$) : ")
     data = data.replace(", BKMEA Membership Number : ", "\nBKMEA Membership Number : ")
     data = data.replace(", Membership Type : ,", "\nMembership Type : ")
     data = data.replace(", Year of Registration : ,", "\nYear of Registration: ")
     data = data.replace("Web :", "\nWeb :")
     data = data.replace(", Contact Person Name :", "\nContact Person Name :")
     data = data.replace(", Factory Category :", "\nFactory Category : ")
     data = data.replace(", Number of Machine :", "\nNumber of Machine : ")
     data = data.replace(", Production Capacity :", "\nProduction Capacity : ")
     data = data.replace(", Number of Employee (Workers) :", "\nNumber of Employee (Workers) : ")
     data = data.replace(", Yearly Turnover (In US$) :", "\nYearly Turnover (In US$) :")
     data = data.replace(", Back to Member List, [Home            Member List             Advanced Search', Home', Member List', Advanced Search, [Home', Member List', Advanced Search, [Company Details           Print Download Member Form                      Primary", "\nNew -----> \n")
     data = data.replace(", [Company Name :", "\nCompany Name :")
     data = data.replace(", [BKMEA Membership Number :", "\nBKMEA Membership Number :")
     data = data.replace(", [Membership Type :", "\nMembership Type :")
     data = data.replace(", [Year of Registration :", "\nYear of Registration :")
     data = data.replace('"[      Company Details           Print Feedback Download Member Form                      Primary', "")
     data = data.replace("[Home', Member List', Advanced Search, [Company Details           Print Feedback Download Member Form                      Primary", "")
     data = data.replace("Back to Member List--> Company Details           Print Feedback Download Member Form                      Primary", "New----->\n")
     data = data.replace("[", "")
     data = data.replace("],", "\n")
     print "Done!"
     outfile.write(data)
     outfile.close()