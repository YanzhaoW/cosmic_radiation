# Guidelines to the lab report of Cosmic Radiation 


## Common mistakes to be avoided

- "Earth" means the planet and "earth" means ground.
- In scientific reports, usages of some some pronouns, like "we", "our", "us", must be avoided.
- Citations should be put before the period in the end of each sentence (see [this](https://academia.stackexchange.com/questions/85477/where-should-citations-be-placed-relative-to-punctuation-e-g-full-stops-and-c)). DO NOT put all citations in the end of the paragraph.
- Each plot must be x-axis label and y-axis label. Each label must also contain a unit. For histograms, the unit of y-axis label (counts) should be `per ${Bin_Width}` or `/${Bin_Width}`.
- Any picture in the report must have a place which refers to it.
- The font size in pictures should be roughly as the same as in texts.

## Important suggestions:
- Before submitting the report, please go through the whole report together with your group members. Check whether there is a typo or whether each sentence ends with a period, etc. Since it's quite normal that each group member has different writing skill, reading the report together is a great chance to learn from each other how to write sentences in a clear and comprehensive way.

- Make sure that all aspects of this experiment are covered in the report. But in the mean time, please keep it short and compact. The suggested length of the report is 15 to 20 pages (including reference list in the end).

## Recommended structure of the lab report

**ATTENTION**: the following structure of chapters and chapter names are merely a suggestion. The points under each chapter are some aspects that must be covered in its sections. Feel free to adapt them with your own flavors.

### Chapter 1: Introduction
Some general information of this experiment should be written here **very briefly**, such as what this experiment is about and what kind of measurements are done.

### Chapter 2: Theoretical Background

- History of the discovery of the cosmic radiation (**briefly**)
- Different components of the cosmic radiation (**detailed**)
- What could be the possible angular distribution for muons (**briefly**)
- East-west effect
- Properties of muons  
    *Keywords*: lepton, mass, lifetime, energy loss, Bethe-Bloch formula, minimum ionizing particle

### Chapter 3: Detectors and electronic modules

- Scintillation (plastic) and its principle (**very detailed**)  
    Please see chapter 8, section 1 of [Radiation Detection and Measurement](https://phyusdb.files.wordpress.com/2013/03/radiationdetectionandmeasurementbyknoll.pdf).
- PMT and its principle
- Mechanism of the constant-fraction discriminator (**detailed**)
    * What are the functions of a CFD and why are CFDs needed in this experiment? (HINT: the time-walk effect and the background noise.)
    * What are the outputs of the CFD? (*HINT*: the logical output and constant-fraction shaped signals, the one with a zero-crossing.)
- Logical unit
- Delay module
- Time-amplitude converter (TAC)
- Multi-channel analyser (MCA)

### Chapter 4: Experimental procedures and setups
- Setup for scintillators  
    *Keywords*: Rotatable frames; Distance between two bars
- Setup for CFDs  
    * How to determine the time delay for the CFD?
    * How to determine an optimal value for the threshold of CFDs? 
    * What is the width of the CFD logical output?
- Coincidence verification  
    *Keywords*: cabal length, T-piece
- Setup and cable connections for the muon angular distribution measurement (detailed)  
    * Modules and cable connections
    * How to count the muons coming from a specific zenith angle?
- Setup for the muon velocity measurement (detailed)  
    * Modules and cable connections
    * How to measurement the muon velocity?
    * How to determine the correlation between the channel number and the real time value?
    * Why is a manual delay is needed?
    * How to eliminate the intrinsic unknown time delay in the modules?

### Chapter 5: Results and Analysis
- Determination of the CFD threshold
- Results of muon angular distribution measurement  
    * What is the fitting function for the angular distribution
- East-west coefficient
- Results of muon velocity measurement
    * Spectrum of time differences
    * Explanation of the tail at larger time values
    * What is the fitting function and calculation of the time of muons traveling perpendicularly
    * Calculation of the muon velocity

### Chapter 6: Discussion
A very brief restatement of what have been done in this experiment and what are the relevant results. If the calculated muon velocity is larger than speed of light, what could be the contributing factors for this error?
