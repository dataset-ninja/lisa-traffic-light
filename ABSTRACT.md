To provide a shared basis for comparing traffic light recognition (TLR) systems, the authors publish an extensive public **LISA Traffic Light Dataset** based on footage from US roads. The dataset contains annotated video sequences, captured under varying light and weather conditions using a stereo camera. The database consists of continuous test and training video sequences, totaling 43,007 frames and 113,888 annotated traffic lights. The sequences are captured by a stereo camera mounted on the roof of a vehicle driving under both night- and daytime with varying light and weather conditions.

## Motivation

The effectiveness of transportation systems profoundly influences workforce mobility, environmental conditions, and energy consumption, thereby exerting a significant impact on foreign policy. Given the integral role transportation plays in people's daily lives, its efficiency, safety, and cleanliness directly affect their health and well-being. Future enhancements to transportation systems are anticipated to stem from advancements in sensing, communication, and processing technologies. The advent of the automobile revolution in the early 20th century sparked a dramatic surge in road transportation, overwhelming the capacity of existing road networks to accommodate the escalating traffic volume. In response, traffic control devices (TCD) were developed to facilitate efficient and safe transportation by guiding, regulating, and warning drivers. These TCDs encompass various infrastructure elements, including signs, signaling lights, and pavement markings, aimed at communicating critical information to drivers.

<img src="https://github.com/dataset-ninja/lisa-traffic-light/assets/120389559/b92bc7ab-8225-41bd-bd41-abce72826bbe" alt="image" width="600">

<span style="font-size: smaller; font-style: italic;">Traffic control devices for safe and efficient traffic flow.</span>

Traffic control devices (TCDs) play a crucial role in complex environments like intersections, where a wealth of information needs to be conveyed. Balancing the provision of adequate information with the avoidance of overwhelming and distracting drivers is key. The effectiveness of TCDs hinges on the driver's ability to process the information within the constraints of time and volume. Excessive speed and information overload can lead to errors and stress among drivers.

For TCDs to function optimally, compliance from all road users is essential to prevent potentially hazardous situations. However, there are instances where drivers deliberately ignore TCDs. Research indicates that more than a third of Americans admit to intentionally running red lights in the past month. Non-compliance can stem from various factors such as rushing to beat a light, aggressive driving behaviors, distractions, misunderstandings, or faulty TCDs. While driving is often perceived as effortless due to automation of many tasks, this can lead to drivers being less focused, resulting in delayed reactions to critical events. Conversely, highly attentive driving can also lead to delayed reaction times due to stress, fatigue, or mental overload.

While widespread adoption of autonomous driving remains a distant prospect, lives can be safeguarded through the implementation of driver assistance systems (DAS) capable of monitoring the environment and intervening in critical situations. To effectively support drivers, DAS must compensate for their limitations. For instance, drivers may have difficulty noticing and recognizing certain TCDs. Studies indicate that while speed limit signs are almost always noticed, pedestrian crossing signs are often overlooked. The reaction times of drivers is longest in the center of the interval, where the decision is the most difficult.

<img src="https://github.com/dataset-ninja/lisa-traffic-light/assets/120389559/fbe59202-9de5-4b8b-93cc-192c3b1f1af1" alt="image" width="600">

<span style="font-size: smaller; font-style: italic;">Fused DAS system in intersection scenarios. (a) Turn right on red assistance. (b) Dilemma zone assistance.</span>

## Traffic lights

Traffic lights (TLs) play a vital role in regulating traffic flow by providing clear instructions to drivers regarding the right of way. This allocation of right of way is meticulously designed to minimize conflicts between vehicles and pedestrians traversing intersecting paths. TLs are intentionally conspicuous, employing bright-colored lamps, typically circular or arrow-shaped, housed within uniformly colored containers. The standard TL configuration features the familiar red-yellow-green sequence, with each light indicating whether drivers should halt, prepare to stop, or proceed. However, to address the complexities of various intersections, a range of alternative TL configurations has been developed.

<img src="https://github.com/dataset-ninja/lisa-traffic-light/assets/120389559/043ac944-7c3b-4902-85a9-a1c83547b202" alt="image" width="600">

<span style="font-size: smaller; font-style: italic;">Examples of vertical TLs found in California.</span>

The orientation, color, size, and shape of the container will vary country to country and even city to city.

<img src="https://github.com/dataset-ninja/lisa-traffic-light/assets/120389559/81cbde50-bbf7-4e28-87a0-2c0e60170868" alt="image" width="600">

<span style="font-size: smaller; font-style: italic;">(a) San Diego, California. (b) Cincinnati, Ohio.</span>

Besides the various configurations of TLs, the state sequence is an important characteristic of a TL. For increasing road safety and making it easier for drivers when driving across states, TLs in USA are regulated by the Federal Highway Administration in the Manual on Uniform Traffic Control Devices.

<img src="https://github.com/dataset-ninja/lisa-traffic-light/assets/120389559/95591700-5816-4c18-9bc9-52fa72a06c4f" alt="image" width="600">

<span style="font-size: smaller; font-style: italic;">Basic TL sequence for states: green, yellow, and red.</span>


## Dataset description

Until now no comprehensive survey of traffic light recognition (TLR) research has been published. The authors presented an introductory overview of ongoing work on traffic light detection along with the LISA Traffic Light Dataset. Most published TLR systems are evaluated on datasets which are unavailable to the public. This makes comparison between existing methods and new contributions difficult. The contributions made in this survey paper are thus, fourfold:
1) Clarifying challenges facing TLR systems.
2) Overview of current methods in TLR research.
3) Common evaluation procedure for TLR systems.
4) High resolution, annotated, stereo video dataset.

The LISA Traffic Light Dataset comprises traffic lights (TLs) located in San Diego, California, USA. This dataset offers two daytime and two nighttime sequences for testing purposes. The test sequences entail 23 minutes and 25 seconds of driving through San Diego. Stereo image pairs are captured using Point Grey's Bumblebee XB3 (BBX3-13S2C-60), equipped with three lenses, each capturing images at a resolution of 1280x960. These lenses boast a Field of View (FoV) of 66°. With three lenses, the stereo camera accommodates two different baselines, 12 and 24 cm, with the wider baseline utilized for the LISA Traffic Light Dataset. The stereo images are uncompressed and rectified in real time. The Bumblebee XB3 is positioned centrally on the roof of the vehicle and connected to a laptop via FireWire-800 (IEEE-1394b). In addition to the four test sequences, 18 shorter video clips are provided for training and testing purposes. Manual adjustments were made to the gain and shutter speed to prevent oversaturation and minimize flickering effects from the TLs. For daytime clips, the shutter speed was set to 1/5000 sec with a gain of 0, while for nighttime clips, the shutter speed was 1/100 sec with a gain of 8. Alongside the stereo images, a Triclops calibration file is included, containing the factory calibration data for the Bumblebee XB3 camera used in the dataset.

The LISA Traffic Light Dataset utilizes stereo vision capturing techniques, as stereo vision is widely employed in various computer vision applications, including Traffic Light Recognition (TLR). Each sequence within the dataset is accompanied by manually labeled annotations specifically for the left stereo frame. These annotations encompass essential details such as the frame number, the outlined rectangular area surrounding the illuminated traffic light (TL) lamp, and its corresponding state. Examining a heatmap generated from all annotations within the dataset reveals a consistent trend: the majority of annotations cluster in the upper right portion of the frames, with only a few TLs annotated on the far left side. Consequently, it is prudent to focus the search for traffic lights primarily on the upper regions of the frames.

<img src="https://github.com/dataset-ninja/lisa-traffic-light/assets/120389559/2205e251-cac8-4cce-8cd8-a803e1d750dc" alt="image" width="600">

<span style="font-size: smaller; font-style: italic;"> Aspect ratio histogram of LISA TL Dataset.</span>

