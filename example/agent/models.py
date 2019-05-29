from django.contrib.auth.models import User

from django.db import models


class Agent(User):
    category = models.PositiveSmallIntegerField(choices=((0, 'Dealer'), (1, 'API Customer')), default=0)
    payment_policy = models.PositiveSmallIntegerField(choices=((0, 'Prepaid'), (1, 'Post-paid'), (2, 'Direct Payment')))
    credit_limit = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    limit_hotel = models.BooleanField(default=False)

    ip_address = models.GenericIPAddressField(null=True, blank=True)
    domain = models.CharField(max_length=255, blank=True)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.PROTECT)
    commission_pct = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(0, 7)], default=0)
    can_create_sub_dealer = models.BooleanField(default=False, verbose_name='Can Create Sub-dealer?')

    class Meta:
        verbose_name = 'Agent'

    def __str__(self):
        return self.get_full_name()


class TopUp(models.Model):
    agent = models.ForeignKey(Agent, on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    status = models.PositiveSmallIntegerField(choices=((0, 'Draft'), (1, 'Pending'), (2, 'Approved'), (3, 'Reject')), default=0)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='created_top_ups', null=True, blank=True)
    payment_mode = models.IntegerField(choices=((0, 'Cash'), (1, 'bKash'), (2, 'CreditCard'), (3, 'Cheque')),
                                       default=0)
    approved_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='approved_top_ups', null=True, blank=True)





