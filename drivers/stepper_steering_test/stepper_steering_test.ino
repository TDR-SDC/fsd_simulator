#include <ArduinoHardware.h>
#include <ros.h>
#include <Stepper.h> 
#include <geometry_msgs/Twist.h>
#define Pi 3.14159265


// Define stepper motor connections and motor interface type. Motor interface type must be set to 1 when using a driver
const int stepsPerRevolution = 150;
// Create Instance of Stepper library
Stepper myStepper(stepsPerRevolution, 8, 9, 10, 11);

// For Steering Stepper
float theta = 0; // Target steering angle/
int curr_steer = 0; // current Steering angle
int step_multiplier = 6; // Multiplier for Gear Ratio
float speed_ang = 0;
float speed_lin = 0;


ros::NodeHandle nh;

void messageCb( const geometry_msgs::Twist& msg){
  speed_ang = msg.linear.y;
  speed_lin = msg.linear.x;
}

ros::Subscriber<geometry_msgs::Twist> sub("steervel_pub", &messageCb );
 

void setup() {
  // put your setup code here, to run once:
  Serial.begin(57600);
  nh.getHardware()->setBaud(57600);

  //Stepper
  myStepper.setSpeed(30);
  // Node
  nh.initNode();
  nh.subscribe(sub);
  myStepper.step(100);////
}

 

void loop() {
  
  // Step_count the final angle for steering to move
  theta = speed_ang * 180/Pi;
  int step_count  = theta - curr_steer;
  int final_steps = step_count * step_multiplier;

//  myStepper.step(final_steps);/
  
  curr_steer = theta;
  for (int i = 0; i< 1; i++){
      myStepper.step(-200);
//      Serial.println(i);
      delay(10);
  }
  for (int i = 0;i < 1; i++){
      myStepper.step(200);
      delay(10);}
  nh.spinOnce();
  delay(1);

}
