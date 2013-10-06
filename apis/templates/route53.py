ChangeResourceRecordSetsTemplate = """<?xml version="1.0" encoding="UTF-8"?>
<ChangeResourceRecordSetsRequest xmlns="https://route53.amazonaws.com/doc/%(Version)s/">
   <ChangeBatch>
      <Changes>
         <Change>
            <Action>%(Action)s</Action>
            <ResourceRecordSet>
               <Name>%(Name)s</Name>
               <Type>%(Type)s</Type>
               <TTL>%(TTL)s</TTL>
               <ResourceRecords>
                  <ResourceRecord>
                     <Value>%(Value)s</Value>
                  </ResourceRecord>
               </ResourceRecords>
            </ResourceRecordSet>
         </Change>
      </Changes>
   </ChangeBatch>
</ChangeResourceRecordSetsRequest>
"""
