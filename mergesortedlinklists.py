def mergeTwoSortedLinkedLists(head1, head2):
    if(head1==None and head2==None):
        return None
    elif(head2==None):
        #If the second list is empty
        return head1
    elif(head1==None):
        #If the first list is empty
        return head2
    else:
        #Creating a new head
        head=None
        last=None
        #Initialising the heads of list1 and list2
        temp1=head1
        temp2=head2
        #Traversing List1 and List2
        while(temp1 is not None and temp2 is not None):
            if(temp1.data<=temp2.data):
                if(head==None):
                    head=temp1
                    last=temp1
                    temp1=temp1.next
                    last.next=None
                else:
                    last.next=temp1
                    last=temp1
                    temp1=temp1.next
                    last.next=None
            else:
                 if(head==None):
                     head=temp2
                     last=temp2
                     temp2=temp2.next
                     last.next=None
                 else:
                     last.next=temp2
                     last=temp2
                     temp2=temp2.next
                     last.next=None
        if(temp1 is None):
            last.next=temp2
        elif(temp2 is None):
            last.next=temp1
        return head