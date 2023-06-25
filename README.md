# Guidelines to the lab report about Cosmic Radiation 


## Common mistakes to be avoided

- "Earth" means the planet and "earth" means ground.
- In scientific reports, usages of pronouns, like "we", "our" or "us" should be avoided.
- Citations should be placed at the end of each sentence before the period (see [this](https://academia.stackexchange.com/questions/85477/where-should-citations-be-placed-relative-to-punctuation-e-g-full-stops-and-c)). DO NOT put all citations at the end of the paragraph.
- Each plot must have a x-axis and y-axis label. Each label must also contain a unit. In case of histograms, the unit of the y-axis label (counts) should be `per ${Bin_Width}` or `/${Bin_Width}`.
- Any picture in the report must be referred to somewhere in the text.
- The font size in pictures should be roughly the same as in the text.

## Important suggestions
- Before submitting the report, please go through it together with your group members. Check whether there are typos or whether each sentence ends with a period, etc. Since it's quite normal for each group member to have a different writing skill, reading the report together is a great opportunity to learn from each other about how to write sentences in a clear and comprehensive way.

- Make sure all aspects of the experiment are covered in the report, while also keeping it short and compact. The suggested length of the report is 15 to 20 pages (including a reference list at the end).

## Recommended structure of the lab report

**ATTENTION**: The following structure of chapters and chapter names are merely a suggestion. The points under each chapter are aspects that should better be covered. Feel free to add your own ideas.

### Chapter 1: Introduction
Some general information about this experiment should be written here **very briefly**, such as what this experiment is about and what kind of measurements are done.

### Chapter 2: Theoretical Background

- History of the discovery of cosmic radiation (**briefly**)
- Different components of cosmic radiation (**detailed**)
- What could be the possible angular distribution of muons (**briefly**)
- East-west effect
- Properties of muons  
    *Keywords*: lepton, mass, lifetime, energy loss, Bethe-Bloch formula, minimum ionizing particle

### Chapter 3: Detectors and electronic modules

- Scintillation (plastic) and its principle (**very detailed**)  
    Please see chapter 8, section 1 of [Radiation Detection and Measurement](https://phyusdb.files.wordpress.com/2013/03/radiationdetectionandmeasurementbyknoll.pdf).
- PMT and its principle
- Mechanism behind a constant-fraction discriminator (**detailed**)
    * What are the functions of a CFD and why are CFDs needed in this experiment? (*HINT*: the time-walk effect and background noise)
    * What are the outputs of a CFD? (*HINT*: the logical output and constant-fraction shaped signals, the one with zero-crossing)
- Logical unit
- Delay module
- Time-amplitude converter (TAC)
- Multi-channel analyser (MCA)

### Chapter 4: Experimental procedures and setups
- Setup for scintillators  
    *Keywords*: rotatable frames, distance between two bars
- Setup for CFDs
    * How to determine the time delay for the CFD?
    * How to determine an optimal value for the threshold of the CFDs? 
    * What is the width of the logical output of the CFD?
- Coincidence verification  
    *Keywords*: cable length, T-piece
- Setup and cable connections for the muon angular distribution measurement (**detailed**)
    * Modules and cable connections
    * How to count the muons coming from a specific zenith angle?
- Setup for the muon velocity measurement (**detailed**)
    * Modules and cable connections
    * How to measure the muon velocity?
    * How to determine the correlation between the channel number and the real time value?
    * Why is a manual delay needed?
    * How to eliminate the intrinsic unknown time delay in the modules?

### Chapter 5: Results and Analysis
- Determination of the CFD threshold
- Results of the muon angular distribution measurement  
    * What is the fitting function for the angular distribution?
- East-west coefficient
- Results of the muon velocity measurement
    * Spectrum of time differences
    * Explanation of the tail at larger time values
    * Fitting function and calculation for the time of perpendicularly traveling muons?
    * Calculation of the muon velocity

### Chapter 6: Discussion
A very brief restatement of what has been done in this experiment and the relevant results. If the calculated muon velocity is larger than the speed of light, what could be contributing factors of this error?
