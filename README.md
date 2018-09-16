In this project we use Django User model. Which allows us to start working with users right away, as
we just did with our Blog app. for Big project Django highly recommends using a custom user model for new projects. The
reason is that if you want to make any changes to the User model down the road–-for
example adding an age field-–using a custom user model from the beginning makes
this quite easy. But if you do not create a custom user model, updating the default
User model in an existing Django project is very, very challenging.
So always use a custom user model for all new Django projects. However the official
documentation example is not actually what many Django experts recommend. It uses
the quite complex AbstractBaseUser when if we just use AbstractUser things are far
simpler and still customizable.
so in next we're gone use custom Django User model


                                                                                                -Santosh Rana
