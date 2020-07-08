print("Enter Base Value:")
Base=int(input())
print("Enter Expo value:")
Expo=int(input())
final_val=1
while Expo>0:
    if Expo%2!=0:
      final_val=final_val*Base
    Base=Base*Base
    Expo>>=1
print(final_val)
