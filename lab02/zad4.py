#Datetime
from datetime import datetime
dt = datetime(2023, 5, 4, 17, 15)
print(dt)

#Padding
print('{:_>20}'.format('Padding'))

#Truncating long strings
print(f'{"przeintelektualizować ":.7}')

#Truncating and align 
print('{:_<20.7}'.format('przeintelektualizować'))

#Named placeholders
data = {'first': 'Placki!', 'last': 'Lubie'}
print('{last} {first}'.format(**data))
