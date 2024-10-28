# 2DT902 : Project : [Samuel Berg(sb224sc)](mailto:sb224sc@student.lnu.se)

[link to document on gdrive](https://docs.google.com/document/d/1H6UAzhqQBWQc88c6wg2Y2SLOo98k4P8d5MFhyZ5edHs/edit?pli=1&tab=t.0)

## Images

![decomp](./img/decompostion.drawio.png)

![sub-sys1](./img/sub-system1.drawio.png)

![sub-sys2-3](./img/sub-system2-3.drawio.png)

![component](./img/component.drawio.png)

## Report template

### Persistence

#### QAS 1 : Data Availability 

**Source**: Unexpected power outage.

**Stimulus**: The system is restarted after an unexpected power outage.

**Artifact**: Web-server.

**Environment**: System has just recovered from an unexpected shutdown.

**Response**: The system should restore all the data exactly as it was before the outage, with no data loss or corruption.

**Response Measure**: All data is accessible and system is fully operational within x minutes.

#### QAS 2 : Data Integrity

**Source**: An Employee.

**Stimulus**: An employee updates the price of a product in the inventory.

**Artifact**: Web-server.

**Environment**: System is fully operational.

**Response**: The system ensures that the price update is reflected across all orders, reports, and inventory views. The old price is archived (logs).

**Response Measure**: The update is applied across the system within 2 seconds (MySQL/PostgresSQL).

#### QAS 3 : System Maintenance

**Source**:

**Stimulus**:

**Artifact**:

**Environment**:

**Response**:

**Response Measure**:

### Solutions

#### QAS 1 : Data Availability 

##### **Alternative 1:**

**Pros:**

-

**Cons:**

-

##### **Alternative 2:**

**Pros:**

-

**Cons:**

-

##### **Our choice:**

#### QAS 2 : Data Integrity

##### **Alternative 1:**

**Pros:**

-

**Cons:**

-

##### **Alternative 2:**

**Pros:**

-

**Cons:**

-

##### **Our choice:**

#### QAS 3 : System Maintenance

##### **Alternative 1:**

**Pros:**

-

**Cons:**

-

##### **Alternative 2:**

**Pros:**

-

**Cons:**

-

##### **Our choice:**

#### Security components

##### **XXX component**

###### **Responsibilities:**

###### **Provides:**

###### **Requires:**

###### **Choice of technology/software:**


##### **XXX component**

###### **Responsibilities:**

###### **Provides:**

###### **Requires:**

###### **Choice of technology/software:**


### Logging

#### QAS 1 : System Error 

**Source**:

**Stimulus**:

**Artifact**:

**Environment**:

**Response**:

**Response Measure**:

#### QAS 2 : Data Modification

**Source**:

**Stimulus**:

**Artifact**:

**Environment**:

**Response**:

**Response Measure**:

 #### QAS 3 : Transaction

**Source**:

**Stimulus**:

**Artifact**:

**Environment**:

**Response**:

**Response Measure**:

### Solutions

#### QAS 1 : System Error 

##### **Alternative 1:**

**Pros:**

-

**Cons:**

-

##### **Alternative 2:**

**Pros:**

-

**Cons:**

-

##### **Our choice:**

#### QAS 2 : Data Modification

##### **Alternative 1:**

**Pros:**

-

**Cons:**

-

##### **Alternative 2:**

**Pros:**

-

**Cons:**

-

##### **Our choice:**

#### QAS 3 : Transaction

##### **Alternative 1:**

**Pros:**

-

**Cons:**

-

##### **Alternative 2:**

**Pros:**

-

**Cons:**

-

##### **Our choice:**

#### Security components

##### **XXX component**

###### **Responsibilities:**

###### **Provides:**

###### **Requires:**

###### **Choice of technology/software:**


##### **XXX component**

###### **Responsibilities:**

###### **Provides:**

###### **Requires:**

###### **Choice of technology/software:**


### Security

#### QAS 1 : Unauthorized Access Attempt 

**Source**:

**Stimulus**:

**Artifact**:

**Environment**:

**Response**:

**Response Measure**:

#### QAS 2 : Multiple Failed Login Attempts

**Source**:

**Stimulus**:

**Artifact**:

**Environment**:

**Response**:

**Response Measure**:

 #### QAS 3 : Denial of Service Protection

**Source**:

**Stimulus**:

**Artifact**:

**Environment**:

**Response**:

**Response Measure**:

### Solutions

#### QAS 1 : Unauthorized Access Attempt 

##### **Alternative 1:**

**Pros:**

-

**Cons:**

-

##### **Alternative 2:**

**Pros:**

-

**Cons:**

-

##### **Our choice:**

#### QAS 2 : Multiple Failed Login Attempts

##### **Alternative 1:**

**Pros:**

-

**Cons:**

-

##### **Alternative 2:**

**Pros:**

-

**Cons:**

-

##### **Our choice:**

#### QAS 3 : Denial of Service Protection

##### **Alternative 1:**

**Pros:**

-

**Cons:**

-

##### **Alternative 2:**

**Pros:**

-

**Cons:**

-

##### **Our choice:**

#### Security components

##### **XXX component**

###### **Responsibilities:**

###### **Provides:**

###### **Requires:**

###### **Choice of technology/software:**


##### **XXX component**

###### **Responsibilities:**

###### **Provides:**

###### **Requires:**

###### **Choice of technology/software:**



## Overview
