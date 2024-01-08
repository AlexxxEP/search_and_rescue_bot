SEARCH AND RESCUE BOT - SYSTEM REQ. SPECIFICATION
============================================
>*This document defines the input rules that defines the development of this project.*
>
>*The document is structured as follows :*
>
> * *`Main problem` : instructions of the project, directly imported from the [instructions provided by the school][Project Instructions] .*
> 
> * *`Application environment` : list of the environmental constraints of the end application. In other words, these are the specifications that encapsulate the project, and hence are common to all levels of validation.*
> 
> * *`Input specifications` : list of the high-level requirements of the project, according to the different levels of validation. (namely: bronze, silver and gold)*
>


## Main problem

Create a robot that can **search**, **find** and **rescue** a **defined object**.



## Application environment / System Constraints

These system constraints are denoted as **EC-*X.Y*** as in Environmental Constraint, where *X* is the ID#
of the constraint category, and *Y* is the ID# of the parameter of its respective constraint category.

#### EC1 - Area
| ID# 					| Constraint title				| Value 						|  
| ---- 					| ----							| -------						|  
| EC-1.1 				| Shape 						| Square						|  
| EC-1.2 				| Size 							| 1.5x1.5m						| 
| EC-1.3 				| Level							| Flat							| 
| EC-1.4 				| Delimitation type 			| Tape							|  
| EC-1.5 				| Delimitation color			| Black							|

#### EC2 - Target
| ID# 					| Constraint title				| Value 						|   
| ---- 					| ----							| -------						|  
| EC-2.1 				| Target shape 					| Cylindrical					|
| EC-2.2 				| Target diameter 				| 10cm max						| 
| EC-2.3 				| Target height 				| 5cm min						|
| EC-2.4 				| Target weight 				| -?-							|
| EC-2.5 				| Target color 					| -?-							|

#### EC3 - Starting position
| ID# 					| Constraint title				| Value 						|   
| ---- 					| ----							| -------						|  
| EC-3.1 				| Start position 				| Any corner of area			|
| EC-3.2 				| Start angle 					| Free							|



## Input specification

These specifications are denoted as **IS-*XY*** as in Input Specification, and describe the system requirements from
a functional perspective. *X* represents the level of validation (*B*:bronze, *S*:silver or *G*:gold) and *Y* represents the ID# of
the said specification. These high level specifications are used to define the [technical specifications][Technical Specs] while sorting
them according to the function they are supposed to achieve.

| ID# 					| Specification													| Source 								|  
| ---- 					| ----															| -------								|  
| IS-100 				| The robot shall autonomously explore the area 				| [Bronze req.][Project Instructions]	|
| IS-200 				| The robot shall detect the target								| [Bronze req.][Project Instructions]	|
| IS-300 				| The robot shall travel to start pos. after target detection	| [Bronze req.][Project Instructions]	|
| IS-400				| The robot shall pick the target up upon target detection		| [Silver req.][Project Instructions]	|
| IS-500 				| The robot shall drop the target at start position				| [Silver req.][Project Instructions]	|
| IS-600 				| The search pattern shall be selectable among 3 patterns		| [Silver req.][Project Instructions]	|
| IS-700 				| The search pattern shall be selectable remotely				| [Gold req.][Project Instructions]		|
| IS-800 				| The robot shall communicate through remote CLI 				| [Gold req.][Project Instructions]		|


## References
+ [Project Instructions][Project Instructions]
+ [Technical Specifications][Technical Specs]


[Project Instructions]: https://github.com/AlexxxEP/search_and_rescue_bot/tree/main/docs/Instructions/2023_Tests_Search%26Rescue.pdf
[Technical Specs]: https://github.com/AlexxxEP/search_and_rescue_bot/tree/main/docs/specifications/technical_specifications.md