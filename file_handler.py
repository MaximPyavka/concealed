import csv

field_names = {'BusinessInfo', 'KidsInfo', 'HomeCountryId', 'CoStateId', 'PeriodLeftId', 'SocialInnovatorsParticipant',
               'data', 'ModifiedOn', 'IndustryIdName', 'MasterProgramName', 'CoEmail', 'MailSendLocationIdName',
               'CoStateIdName', 'SpouseLastName', 'PhotoUrl', 'IncSubscription', 'CoCompanyId', 'ChapterIdName',
               'PositionIdName', 'AcceleratorProgramIdName', 'URL', 'AssistPhoneCode', 'ContactId', 'BusDesc',
               'Biography', 'ReasonForHoldIdName', 'DirectPhoneExt', 'Year', 'MI', 'LeadSource', 'OptedOutOfForums',
               'FirstName', 'PrimaryChapterAreaRegion', 'KidsName', 'IsGlobalStaff', 'IndustryId', 'FiscalYearId',
               'Suffix', 'IsChapterOfficer', 'MainPhone', 'OptoutofEmailNewsletters', 'SocialMediaInfo',
               'LeadSourceIdName', 'QualificationStatusId', 'User_MemberID', 'PreferedPhoneNumberType', 'CellPhone',
               'HomeStateIdName', 'CellPhoneCode', 'RoleXml', 'Referral', 'OnlineTrained', 'SocialMediaId',
               'SpouseForumId', 'KidsNumber', 'PreferredPhone', 'LeadershipId', 'RequalificationFormReceived',
               'TitleCo', 'NickName', 'DateFounded', 'MethodOfPaymentId', 'PrimaryChapterId',
               'PrimaryChapterAreaRegionDisplay', 'ForumTrained', 'PagerCode', 'ApplicationUrl', 'PersonalInfo',
               'EOGroupsInfo', 'PreferredPhoneExt', 'SocialMediaIdName', 'MentorName', 'FTE', 'TypeIdName',
               'SecurityQuestionAnswer', 'PrimaryChapterIdName', 'MentorProgramParticipantId', 'SpouseEmail',
               'CreatedOn', 'SentByIdName', 'MemberId', 'MemberIdName', 'SecurityQuestionID', 'PositionId',
               'CreatedByIdName', 'IsOnDemandOptOut', 'MainPhoneCode', 'AssistPhone', 'ParentId', 'AssistEmail',
               'RoleInBusIdName', 'FaxCode', 'MasterProgramID', 'DirectPhoneCode', 'HomeCity', 'CoAddressL1',
               'CompanyIdName', 'IsMemberKitSent', 'RequalificationFormRecv', 'MentorEndDate', 'Pager', 'GenderIdName',
               'CoCity', 'AcceleratorIdName', 'HidePersonalInfo', 'HomeFax', 'CommPref', 'MemberChapterInfo',
               'PeriodJoinedId', 'HomeStateId', 'SocialMediaConnectionId', 'QualificationStatusIdName',
               'PeriodJoinedIdName', 'SentById', 'OtherOrgsId', 'IconUrl', 'Company', 'SalesAmount',
               'ReasonForLeavingIdName', 'IncSubscriptionDate', 'OnDemandOptOut', 'PreferredName', 'SpouseBusinessInfo',
               'DirectPhone', 'CurrentCompany', 'AdminInfo', 'SpouseForumIdName', 'OctaneDeliveryIdName',
               'HomeAddressL2', 'ForumTrainerIdName', 'ClassroomTrainedDate', 'MemberStatusId', 'CoAddressL2',
               'ChapterId', 'ForumMembershipIdName', 'ForumTrainerId', 'PrimaryChapterArea', 'HomeAddressL1',
               'OtherLeadSource', 'SalesInfo', 'RoleTitles', 'GlobalLeadershipInfo', 'Isfollowupcallmade',
               'InterestsInfo', 'MailSendLocationId', 'FollowUpCallMadeDate', 'ChapterLeadershipInfo', 'HomePhoneCode',
               'PreferredPhoneCountryCode', 'AcceleratorId', 'ChildId', 'LeadSourceId', 'MentorOrganizationIdName',
               'Preference', 'IsGlobalLeader', 'SpouseFirstName', 'IsPacketSent', 'BenefitsInfo', 'ForumMembershipId',
               'MemberKitSent', 'ModifiedByIdName', 'Fax', 'MentorProgramParticipantIdName', 'CompanySalesId',
               'MentorOrganizationId', 'HomePostalCode', 'MemberStatusIdName', 'SecurityQuestionIDName', 'DOB',
               'HideBusinessInfo', 'MemberExchID', 'CoCountryIdName', 'ReasonForHoldId', 'RenewalInfo', 'HomeFaxCode',
               'OtherOrgsIdName', 'ReasonForLeavingId', 'PrimarymethodforreceivingMailWeb', 'CoPostalCode',
               'HomeCountryIdName', 'Name', 'MentorStartDate', 'Colleges', 'ModeratorTrained', 'MemberExchangeIdName',
               'CoCountryId', 'AcceleratorProgramId', 'PeriodLeftIdName', 'LastName', 'MembershipInfo',
               'OctaneDeliveryId', 'IncludeInSearch', 'CompanyId', 'MethodOfPaymentIdName', 'HomePhone',
               'MemberExchangeId', 'MemberSince', 'CommunicationviatextSMS', 'Email', 'CoURL', 'RoleInBusId',
               'SOSMembership', 'GenderId', 'DatePacketSent', 'FiscalYearIdName', 'MProfileType',
               'IsAcceleratorGraduate', 'TypeId', 'AssistName'}


class CSVWriterContextManager:
    def __init__(self, filename, field_names):
        self.csv_file = filename
        self.field_names = field_names
        self.mode = 'w'
        self.new_line = ''
        self.writer = None

    def __enter__(self):
        self.out_file = open(self.csv_file, self.mode, newline=self.new_line)
        self.writer = csv.DictWriter(self.out_file, delimiter=',', fieldnames=self.field_names)
        self.writer.writeheader()
        self.writer.fieldnames = self.field_names
        return self.writer

    def __exit__(self, exc_type, exc_value, traceback):
        self.out_file.close()


if __name__ == '__main__':
    file = 'res.csv'
    with CSVWriterContextManager(file, field_names) as res:
        row = {'Suffix': 1324234, }
        res.writerow(row)
