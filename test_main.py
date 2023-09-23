import zeep
from zeep import Client
from zeep.xsd import Element, ComplexType, Sequence, AnyType
from zeep.xsd.valueobjects import CompoundValue

import logging
from sqlalchemy import create_engine, select, insert, or_, func
from sqlalchemy.orm import relationship, backref, sessionmaker
from datetime import datetime, timedelta
from lxml import etree


# Request a new call be created
def create_new_call(call):
    try:
        client = Client("create_works_orders_definition.wsdl")
        with client.settings(strict=False, xml_huge_tree=True, xsd_ignore_sequence_order=True):
            # Define the SX3_XML_DOCUMENT element
            SX3_XML_DOCUMENT = client.get_element('SX3_XML_DOCUMENT')



            # Define the body parameters (replace with actual values)
            CreateWorksOrders = client.get_element('{http://www.sx3.com/CREATE_WORKS_ORDERS}CreateWorksOrders')
            body_data = CreateWorksOrders(
                WOR=dict(
                    SrqNo=12345,  # Example value
                    ExternalReference='YOUR_EXTERNAL_REFERENCE',
                    WorkProgramme='YOUR_WORK_PROGRAMME',
                    ContractorSite='YOUR_CONTRACTOR_SITE',
                    PriorityCode='YOUR_PRIORITY_CODE',
                    LocationNotes='YOUR_LOCATION_NOTES',
                    AccessNotes='',
                    AccessAm='',
                    AccessPm='',
                    WoDescription='YOUR_WO_DESCRIPTION',
                    Jobs=dict(
                        Job=[
                            dict(
                                JobSorCode='',
                                JobPriorityCode='',
                                JobQuantity='',
                                JobOrderSequence='',
                                JobLocationNotes='',
                                JobRechargeLiabilityInd='',
                            )
                        ]
                    ),
                )
            )

            # Construct the SX3_BODY element
            SX3_BODY = client.get_element('SX3_BODY')
            sx3_body_data = SX3_BODY(
                CreateWorksOrders=body_data
            )

            # Construct the full request data
            request_data = SX3_XML_DOCUMENT(
                SX3_HEADER=dict(
                    API='YOUR_API_VALUE',
                    REQUESTOR='YOUR_REQUESTOR_VALUE',
                    REQUEST_USER='YOUR_REQUEST_USER_VALUE',
                    REQUEST_PASSWORD='YOUR_REQUEST_PASSWORD_VALUE'
                ),
                SX3_BODY=sx3_body_data
            )
            response = client.service.CreateWorksOrders(request_data)



    except Exception as ex:
        return False

    if (response.MESSAGE_RETURN_INFO.SUCCESS_FLAG and response.CreateWorksOrdersResponse.APIReturn == "SUCCESS"):
        return True


if __name__ == "__main__":
    callmodel = []
    create_new_call(callmodel)