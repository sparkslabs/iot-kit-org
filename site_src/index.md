# IOT-KIT
## An IOT Stack for an Internet of Things of Yours

IOT-KIT is a toolkit for adding connectivity to devices in a standardised
manner so that they can be discovered, queries, controlled and
internetworked.  The primary purpose of this domain is to provide a link
back to the toolkit, and to define the types used in the toolkit.

The protocol it speaks is called "iotoy" - which stands for "Internet Of
Things Of Yours"

The toolkit can be found here on github:

* <https://github.com/sparkslabs/iot-kit>

The types used within the iotoy protocols are defined below here:

* <http://iotoy.org/types/>

You can create types for your devices though trivially.

If you browse those types

* using a browser you get HTML pages (due to the Accept: header
  mentioning text/html)

* using software (such as the python requests library etc) you get
  back application/json representations instead.

## What job does this do?

This project allows you to take networked control of the IOT devices that
you own in a standardised manner, allowing them to be combined together to
form useful systems.

It allows you to create new devices with IOT capabilities trivially, and
allows you to work with devices that have IOToy capabilities trivially.
Be they robots, toys, or coffee machines.

### What does it provide?

It provides the following:

* A standard low level serial based API for query and control of IOT devices.
* A simple set of libraries to use to augment your device with that
* Python code for directly interacting with such devices trivially.
* An RESTful API mapping for taking IOT devices and publishing their
  capabilities onto the local network
* Python libraries for implementing this API trivially
* Python libraries for seeking out IOToy devices on the local network and
  using them trivially.

The guiding philosophy of each part of the API is that it should be usable
by casual and novice developers. For example, if you already have a functioning
Arduino style device, the time to take that and put that on the local network
is around 20-30 minutes. (Assuming familiarity with the libraries)

Example devices created using IOToy:

* Sumobot robots suitable for use with scouting groups
* Child programmable & wearable LED matrix badges. ( [BBC Micro:bit][MICROBIT] )

[MICROBIT]: http://www.bbc.co.uk/rd/blog/2015/07/prototyping-the-bbc-microbit


## Example usage of Web API:

<pre>
from iotoy.local import robot

ON = 1
robot.forward()
robot.led = ON
if robot.sensor >255:
   robot.forward()

print robot.sensor.__doc__
</pre>


## Sample Device Description Derived from Device

This API is entirely derived from the device itself, and used to automatically 
create the sort of Web API above.


<pre>
$ python
Python 2.7.6 (default, Mar 22 2014, 22:59:56) 
[GCC 4.8.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> from iotoy.local import testhosttiny
>>> testhosttiny
<iotoy.discovery.testhosttiny object at 0x7f7add452350>
>>> help(testhosttiny)
{ Screen shows help from the introspected device }
>>> pprint.pprint(testhosttiny.devinfo)
{u'attrs': {u'drive_forward_time_ms': {u'help': u'How long to move forward',
                                       u'href': u'/drive_forward_time_ms',
                                       u'type': u'int'},
            u'ratio': {u'help': u'Sample float attribute',
                       u'href': u'/ratio',
                       u'type': u'float'},
            u'some_flag': {u'help': u'Sample bool attribute',
                           u'href': u'/some_flag',
                           u'type': u'bool'},
            u'str_id': {u'help': u'Sample str attribute',
                        u'href': u'/str_id',
                        u'type': u'str'},
            u'turn_time_ms': {u'help': u'How long to turn',
                              u'href': u'/turn_time_ms',
                              u'type': u'int'}},
 u'devicename': u'testhosttiny',
 u'funcs': {u'barecommand': {u'help': u'test, basic command, no arg/result',
                             u'href': u'/barecommand',
                             u'type': 'iotoy.org/types/function',
                             u'value': {u'name': u'barecommand',
                                        u'spec': {u'args': [],
                                                  u'result': []}}},
            u'no_arg_result_T': {u'help': u'test, one arg, generic type',
                                 u'href': u'/no_arg_result_T',
                                 u'type': 'iotoy.org/types/function',
                                 u'value': {u'name': u'no_arg_result_T',
                                            u'spec': {u'args': [],
                                                      u'result': [[u'result',
                                                                   u'T']]}}},
            u'no_arg_result_bool': {u'help': u'test, one arg, boolean',
                                    u'href': u'/no_arg_result_bool',
                                    u'type': 'iotoy.org/types/function',
                                    u'value': {u'name': u'no_arg_result_bool',
                                               u'spec': {u'args': [],
                                                         u'result': [[u'result',
                                                                      u'bool']]}}},
            u'no_arg_result_float': {u'help': u'test, one arg, float',
                                     u'href': u'/no_arg_result_float',
                                     u'type': 'iotoy.org/types/function',
                                     u'value': {u'name': u'no_arg_result_float',
                                                u'spec': {u'args': [],
                                                          u'result': [[u'result',
                                                                       u'float']]}}},
            u'no_arg_result_int': {u'help': u'test, one arg, integer',
                                   u'href': u'/no_arg_result_int',
                                   u'type': 'iotoy.org/types/function',
                                   u'value': {u'name': u'no_arg_result_int',
                                              u'spec': {u'args': [],
                                                        u'result': [[u'result',
                                                                     u'int']]}}},
            u'no_arg_result_str': {u'help': u'test, one arg, string',
                                   u'href': u'/no_arg_result_str',
                                   u'type': 'iotoy.org/types/function',
                                   u'value': {u'name': u'no_arg_result_str',
                                              u'spec': {u'args': [],
                                                        u'result': [[u'result',
                                                                     u'str']]}}},
            u'one_arg_T': {u'help': u'test, one arg, generic type',
                           u'href': u'/one_arg_T',
                           u'type': 'iotoy.org/types/function',
                           u'value': {u'name': u'one_arg_T',
                                      u'spec': {u'args': [[u'attr', u'T']],
                                                u'result': []}}},
            u'one_arg_bool': {u'help': u'test, one arg, boolean',
                              u'href': u'/one_arg_bool',
                              u'type': 'iotoy.org/types/function',
                              u'value': {u'name': u'one_arg_bool',
                                         u'spec': {u'args': [[u'myarg',
                                                              u'bool']],
                                                   u'result': []}}},
            u'one_arg_float': {u'help': u'test, one arg, float',
                               u'href': u'/one_arg_float',
                               u'type': 'iotoy.org/types/function',
                               u'value': {u'name': u'one_arg_float',
                                          u'spec': {u'args': [[u'myarg',
                                                               u'float']],
                                                    u'result': []}}},
            u'one_arg_int': {u'help': u'test, one arg, integer',
                             u'href': u'/one_arg_int',
                             u'type': 'iotoy.org/types/function',
                             u'value': {u'name': u'one_arg_int',
                                        u'spec': {u'args': [[u'myarg',
                                                             u'int']],
                                                  u'result': []}}},
            u'one_arg_int_result_int': {u'help': u'test, one arg, one result, both ints',
                                        u'href': u'/one_arg_int_result_int',
                                        u'type': 'iotoy.org/types/function',
                                        u'value': {u'name': u'one_arg_int_result_int',
                                                   u'spec': {u'args': [[u'myarg',
                                                                        u'int']],
                                                             u'result': [[u'result',
                                                                          u'int']]}}},
            u'one_arg_str': {u'help': u'test, one arg, string',
                             u'href': u'/one_arg_str',
                             u'type': 'iotoy.org/types/function',
                             u'value': {u'name': u'one_arg_str',
                                        u'spec': {u'args': [[u'myarg',
                                                             u'str']],
                                                  u'result': []}}}}}

</pre>



## Status

The codebase is relatively mature, but light on examples. You can use the system
now to build interesting and useful systems.


## Source

Ongoing development is here:

* <https://github.com/sparkslabs/iot-kit>

As always, feedback, usecases, devices very welcome.


## Ongoing development

The main actual development site (at present) is http://www.sparkslabs.com/iot-kit/


## Ubuntu Packages/etc?

These are available here:

* <http://sparkslabs.com/iot-kit>
