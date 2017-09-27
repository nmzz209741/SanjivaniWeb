# from django.db import models
# from account.models import medicine,batchdata
#
# class viewstore_admin(models.Model):
#     med=models.ForeignKey(medicine, on_delete=models.CASCADE)
#     btdt=models.ForeignKey(batchdata, on_delete=models.CASCADE)
#
#     class Meta:
#         db_table = 'viewstore_admin'
#
#     def __str__(self):
#         return str(self.med) +  str(self.btdt)