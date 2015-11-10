include "baseplate.thrift"

service ToyService extends baseplate.BaseplateService {
  i32 get_random(),
  i32 multiply(1:i32 one, 2:i32 two),
}
