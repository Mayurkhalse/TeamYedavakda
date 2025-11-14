
"""
create_mock_knowledge_base.py
Creates a comprehensive mock knowledge base for BloomWatch chatbot testing
"""

import os
from pathlib import Path

def create_knowledge_base():
    """Create mock agricultural knowledge base with comprehensive content"""
    
    # Create directory structure
    base_path = Path("knowledge_base")
    categories = [
        "satellite_interpretation",
        "crop_health",
        "fertilizers",
        "pest_management",
        "irrigation",
        "weather_impact",
        "crop_suggestions"
    ]
    
    print("🌾 Creating BloomWatch Mock Knowledge Base...")
    print("=" * 60)
    
    for category in categories:
        category_path = base_path / category
        category_path.mkdir(parents=True, exist_ok=True)
        print(f"✅ Created directory: {category_path}")
    
    # Create content for each category
    create_satellite_interpretation(base_path / "satellite_interpretation")
    create_crop_health(base_path / "crop_health")
    create_fertilizers(base_path / "fertilizers")
    create_pest_management(base_path / "pest_management")
    create_irrigation(base_path / "irrigation")
    create_weather_impact(base_path / "weather_impact")
    create_crop_suggestions(base_path / "crop_suggestions")
    
    print("\n" + "=" * 60)
    print("✅ Mock Knowledge Base Created Successfully!")
    print("=" * 60)
    print(f"\n📁 Location: {base_path.absolute()}")
    print(f"📊 Total files: {sum(1 for _ in base_path.rglob('*.txt'))}")
    print("\n🚀 Next steps:")
    print("   1. Run: python document_processor.py")
    print("   2. Run: python main.py")
    print("   3. Test: python test_api.py")

def create_satellite_interpretation(path):
    """Create satellite data interpretation documents"""
    
    # NDVI Guide
    ndvi_content = """
NDVI (Normalized Difference Vegetation Index) - Complete Guide for Farmers

What is NDVI?
NDVI is a vegetation index that uses satellite imagery to measure crop health and vigor. 
It analyzes how plants reflect different wavelengths of light - specifically red and 
near-infrared light - to determine their health status.

NDVI Value Interpretation:
- 0.8 to 1.0: Extremely healthy, dense vegetation (peak growth)
- 0.6 to 0.8: Healthy vegetation (good crop vigor)
- 0.4 to 0.6: Moderately healthy (acceptable but monitor)
- 0.2 to 0.4: Sparse or stressed vegetation (needs attention)
- 0.0 to 0.2: Very poor vegetation or bare soil
- Below 0.0: Water, ice, snow, or non-vegetated surfaces

Crop-Specific NDVI Guidelines for India:

WHEAT:
- Germination stage (0-20 days): NDVI 0.1-0.3
- Tillering stage (20-40 days): NDVI 0.3-0.5
- Jointing stage (40-60 days): NDVI 0.5-0.7
- Heading stage (60-80 days): NDVI 0.7-0.85 (peak)
- Grain filling (80-100 days): NDVI 0.6-0.7
- Maturity (100-120 days): NDVI 0.4-0.5

RICE (PADDY):
- Transplanting (0-15 days): NDVI 0.2-0.3
- Tillering (15-40 days): NDVI 0.4-0.6
- Stem elongation (40-65 days): NDVI 0.6-0.8
- Panicle initiation (65-80 days): NDVI 0.75-0.85 (peak)
- Grain filling (80-100 days): NDVI 0.6-0.7
- Maturity (100-120 days): NDVI 0.3-0.5

COTTON:
- Germination (0-20 days): NDVI 0.1-0.2
- Squaring (20-60 days): NDVI 0.4-0.6
- Flowering (60-90 days): NDVI 0.7-0.85
- Boll development (90-120 days): NDVI 0.6-0.75
- Boll opening (120-150 days): NDVI 0.4-0.5

SOYBEAN:
- Emergence (0-15 days): NDVI 0.1-0.2
- Vegetative growth (15-45 days): NDVI 0.5-0.7
- Flowering (45-65 days): NDVI 0.75-0.85
- Pod development (65-90 days): NDVI 0.7-0.8
- Maturity (90-110 days): NDVI 0.3-0.5

What Low NDVI Indicates:
1. Water stress or drought
2. Nutrient deficiency
3. Pest or disease infestation
4. Poor soil quality
5. Inadequate crop management
6. Natural crop senescence (end of season)

What High NDVI Indicates:
1. Healthy, vigorous growth
2. Adequate water and nutrients
3. Good crop management
4. Optimal growing conditions
5. Dense canopy cover

How to Act on NDVI Data:
- NDVI dropping unexpectedly: Investigate for pests, diseases, or water stress
- NDVI plateauing: Normal if at appropriate growth stage, otherwise check nutrition
- NDVI below expected range: Consider irrigation, fertilization, or pest control
- NDVI consistently low across field: May indicate soil problems or drainage issues
- Variable NDVI within field: Suggests need for precision agriculture approach

Regional Considerations for India:
Maharashtra (Black Soil): Typical NDVI peaks 0.7-0.8
Punjab/Haryana (Alluvial): NDVI peaks can reach 0.8-0.9
Karnataka (Red Soil): NDVI peaks typically 0.6-0.75
Tamil Nadu (Coastal): NDVI may be affected by high humidity, typical peaks 0.65-0.8
"""

    # EVI Guide
    evi_content = """
EVI (Enhanced Vegetation Index) - Detailed Guide for Indian Farmers

What is EVI?
EVI is an optimized vegetation index that improves upon NDVI by being more sensitive to 
high biomass regions and correcting for atmospheric conditions and soil background signals.
It's particularly useful in areas with dense vegetation.

EVI vs NDVI - When to Use Which:
- Use EVI for: Dense crop canopies, high biomass crops, areas with atmospheric interference
- Use NDVI for: General vegetation monitoring, sparse to moderate vegetation, quick assessments
- Use both for: Comprehensive crop health analysis

EVI Value Interpretation:
- 0.6 to 1.0: Very dense, healthy vegetation
- 0.4 to 0.6: Good vegetation health and density
- 0.2 to 0.4: Moderate vegetation
- 0.0 to 0.2: Sparse vegetation or stressed crops
- Below 0.0: Non-vegetated surfaces

Crop-Specific EVI Guidelines:

HIGH BIOMASS CROPS (Sugarcane, Maize):
- Peak EVI values: 0.65-0.75
- EVI is more accurate than NDVI for these crops
- Monitor for sudden drops indicating stress

MEDIUM BIOMASS CROPS (Wheat, Rice, Cotton):
- Peak EVI values: 0.55-0.65
- Good for detecting early stress before visible symptoms

LOW BIOMASS CROPS (Pulses, Vegetables):
- Peak EVI values: 0.4-0.55
- Use in combination with NDVI for best results

Seasonal EVI Patterns in India:

Kharif Season (Monsoon - June to October):
- Rice: EVI peaks at 0.6-0.7 during vegetative growth
- Cotton: EVI reaches 0.55-0.65 at flowering
- Soybean: Peak EVI 0.5-0.6
- Maize: Highest EVI among Kharif crops, 0.65-0.75

Rabi Season (Winter - November to March):
- Wheat: EVI peaks at 0.55-0.65 during stem elongation
- Chickpea: EVI typically 0.45-0.55
- Mustard: EVI around 0.5-0.6

Zaid Season (Summer - March to June):
- Watermelon, Cucumber: EVI 0.4-0.5
- Summer Moong: EVI 0.45-0.55

How to Use EVI Data:

1. Crop Growth Monitoring:
   - Track EVI progression through growing season
   - Compare with expected growth curves
   - Identify areas of underperformance

2. Stress Detection:
   - Sudden EVI drop: Immediate stress (drought, pest attack)
   - Gradual EVI decline: Progressive stress (nutrient deficiency)
   - Persistent low EVI: Fundamental issues (soil, variety)

3. Yield Prediction:
   - Peak EVI values correlate with final yield
   - Higher peak EVI = Higher yield potential
   - Use historical data for your region

4. Irrigation Management:
   - EVI drops below normal: Consider irrigation
   - Maintain EVI within optimal range for crop stage
   - Combine with soil moisture data

5. Fertilizer Decisions:
   - Low EVI mid-season: May need nitrogen application
   - Compare EVI with neighboring fields
   - Use as trigger for foliar nutrient analysis

Interpreting EVI with NDVI Together:

Both High (NDVI >0.7, EVI >0.6):
- Excellent crop health
- Optimal growing conditions
- Continue current management

NDVI High, EVI Moderate:
- Good health but may need nutrients
- Check for micronutrient deficiency
- Consider balanced fertilization

Both Moderate (NDVI 0.4-0.6, EVI 0.3-0.5):
- Acceptable but room for improvement
- Evaluate water and nutrient status
- Compare with crop stage expectations

Both Low (NDVI <0.4, EVI <0.3):
- Significant crop stress
- Immediate investigation needed
- Check for multiple stress factors

NDVI Low, EVI Very Low:
- Severe crop damage or poor establishment
- Consider replanting if very early
- Intensive intervention required

Regional Calibration:
- Black Soil (Maharashtra, MP): EVI typically 5-10% lower than all-India average
- Alluvial Soil (Punjab, UP): EVI can be 5-10% higher
- Red Soil (Karnataka, AP): EVI similar to national average
- Coastal Areas: EVI may show more variation due to humidity

Best Practices:
1. Monitor both NDVI and EVI weekly during critical growth stages
2. Establish baseline values for your farm
3. Compare with previous seasons and neighboring farms
4. Use satellite data in combination with ground observations
5. Act promptly when values deviate significantly from expected
"""

    # Save files
    with open(path / "ndvi_guide.txt", "w", encoding="utf-8") as f:
        f.write(ndvi_content)
    
    with open(path / "evi_guide.txt", "w", encoding="utf-8") as f:
        f.write(evi_content)
    
    print(f"✅ Created satellite interpretation documents in {path}")

def create_crop_health(path):
    """Create crop health monitoring documents"""
    
    content = """
Crop Health Monitoring and Disease Management - Complete Guide

WHEAT CROP HEALTH

Common Diseases:
1. Rust Diseases (Yellow Rust, Brown Rust, Black Rust)
   - Symptoms: Orange/brown pustules on leaves and stems
   - NDVI Impact: Drops from 0.7+ to 0.4-0.5
   - Prevention: Use resistant varieties, proper spacing
   - Treatment: Fungicides (Propiconazole, Tebuconazole)
   - Application: Spray at first sign, repeat after 15 days

2. Powdery Mildew
   - Symptoms: White powdery growth on leaves
   - NDVI Impact: Gradual decline to 0.5-0.6
   - Prevention: Avoid excessive nitrogen
   - Treatment: Sulfur-based fungicides
   - Timing: Early morning or evening application

3. Loose Smut
   - Symptoms: Black powder in ear heads
   - Prevention: Seed treatment with systemic fungicides
   - Treatment: Remove infected plants, use certified seed

Nutrient Deficiency Symptoms in Wheat:
- Nitrogen: Yellowing of lower leaves, stunted growth, NDVI <0.5
- Phosphorus: Purple tint on leaves, poor root development
- Potassium: Scorched leaf margins, weak stems
- Zinc: White/yellow areas between leaf veins

RICE (PADDY) HEALTH

Common Diseases:
1. Blast Disease
   - Symptoms: Diamond-shaped lesions on leaves
   - NDVI Impact: Can drop to 0.3-0.4 in severe cases
   - Critical stages: Tillering and panicle formation
   - Treatment: Tricyclazole or Carbendazim spray
   - Prevention: Balanced fertilization, avoid water stress

2. Bacterial Leaf Blight
   - Symptoms: Water-soaked lesions, leaf wilting
   - NDVI Impact: Rapid decline in affected areas
   - Treatment: Copper-based bactericides
   - Prevention: Use disease-free seeds, proper drainage

3. Sheath Blight
   - Symptoms: Oval lesions on leaf sheaths near waterline
   - Treatment: Validamycin or Hexaconazole
   - Application: Directed spray at lower plant parts

Nutrient Management for Rice:
- Nitrogen: 120-150 kg/ha in split doses (basal, tillering, panicle)
- Phosphorus: 60 kg/ha at planting
- Potassium: 40 kg/ha, split application
- Zinc: 25 kg ZnSO4/ha if deficiency observed

COTTON HEALTH

Common Pests and Diseases:
1. Pink Bollworm
   - Symptoms: Damaged bolls, larvae inside
   - Monitoring: Pheromone traps
   - Treatment: Bt cotton varieties, biopesticides
   - NDVI Impact: Moderate (0.6-0.7 even with infestation)

2. Whitefly
   - Symptoms: Sticky honeydew on leaves, sooty mold
   - NDVI Impact: Significant (drops to 0.4-0.5)
   - Treatment: Neem oil, Imidacloprid, Thiamethoxam
   - Prevention: Avoid excessive nitrogen, maintain field hygiene

3. Fusarium Wilt
   - Symptoms: Wilting, yellowing, vascular browning
   - NDVI Impact: Localized drops visible in satellite imagery
   - Prevention: Resistant varieties, soil treatment
   - Management: Remove infected plants, soil solarization

Cotton Nutrient Requirements (per hectare):
- Nitrogen: 100-150 kg (split in 3-4 doses)
- Phosphorus: 50-60 kg (basal)
- Potassium: 50-60 kg (split)
- Boron: 5 kg (foliar at flowering)

SOYBEAN HEALTH

Common Issues:
1. Yellow Mosaic Virus
   - Vector: Whitefly
   - Symptoms: Yellow patches on leaves
   - NDVI Impact: Reduces to 0.3-0.5
   - Prevention: Control whitefly, use tolerant varieties
   - No cure: Focus on prevention and vector control

2. Rust Disease
   - Symptoms: Reddish-brown pustules on leaves
   - Treatment: Azoxystrobin or Trifloxystrobin
   - Timing: Spray at first appearance

3. Pod Borer
   - Symptoms: Damaged pods, larvae presence
   - Treatment: NPV, Bt-based biopesticides
   - Timing: At flower initiation and pod formation

Integrated Pest Management (IPM) Guidelines:

1. Monitoring and Scouting:
   - Check fields twice weekly during critical stages
   - Use NDVI/EVI to identify problem areas
   - Set up pheromone traps for key pests
   - Record observations systematically

2. Cultural Practices:
   - Crop rotation to break pest cycles
   - Proper spacing for air circulation
   - Timely irrigation to avoid stress
   - Remove crop residues after harvest
   - Border crops as trap crops

3. Biological Control:
   - Encourage beneficial insects (ladybugs, lacewings)
   - Use biopesticides (Bt, NPV, Trichoderma)
   - Neem-based products for pest deterrence
   - Release parasitoids for specific pests

4. Chemical Control (Last Resort):
   - Use only when threshold levels exceeded
   - Rotate chemical groups to prevent resistance
   - Follow recommended dosages strictly
   - Observe pre-harvest intervals
   - Avoid spraying during flowering for pollinator safety

5. Precision Application Based on Satellite Data:
   - Use NDVI maps to identify stressed areas
   - Apply treatments only where needed (spot treatment)
   - Reduces chemical use by 30-50%
   - More economical and environment-friendly

Early Warning Signs of Crop Stress:

Visual + NDVI/EVI Indicators:
1. Water Stress:
   - Wilting during hot hours
   - NDVI drops 10-15% from baseline
   - EVI drops more rapidly than NDVI
   - Action: Immediate irrigation

2. Nutrient Deficiency:
   - Yellowing (nitrogen) or purpling (phosphorus)
   - Gradual NDVI decline over 1-2 weeks
   - Action: Soil test and targeted fertilization

3. Pest/Disease Attack:
   - Spots, lesions, or abnormal growth
   - Sudden NDVI drop in localized areas
   - Action: Identify cause, apply appropriate treatment

4. Heat Stress:
   - Leaf curling, browning
   - NDVI remains stable but growth slows
   - Action: Irrigation, mulching, shade nets if possible

Regional Disease Hotspots in India:
- Punjab/Haryana: Wheat rust (February-March)
- West Bengal/Odisha: Rice blast (August-September)
- Maharashtra/Gujarat: Cotton wilt (July-August)
- Madhya Pradesh: Soybean rust and yellow mosaic (August-September)

Preventive Measures:
1. Use certified, disease-resistant seeds
2. Maintain optimal plant nutrition
3. Ensure proper irrigation (not too much, not too little)
4. Practice crop rotation
5. Monitor satellite indices weekly
6. Keep fields clean of weeds and crop residues
7. Train workers to identify early disease symptoms
8. Maintain farm records for pattern analysis

When to Seek Expert Help:
- Unusual symptoms not matching known issues
- Rapid spread despite treatment
- NDVI/EVI values declining despite interventions
- Multiple stress factors present
- Uncertainty about treatment options
"""

    with open(path / "crop_health_monitoring.txt", "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"✅ Created crop health documents in {path}")

def create_fertilizers(path):
    """Create fertilizer recommendation documents"""
    
    content = """
Comprehensive Fertilizer Management Guide for Indian Crops

UNDERSTANDING NPK AND NUTRIENTS

Primary Nutrients:
1. Nitrogen (N):
   - Role: Leaf and stem growth, protein synthesis, chlorophyll formation
   - Deficiency: Yellowing of older leaves, stunted growth, reduced NDVI
   - Excess: Excessive vegetative growth, lodging, pest susceptibility
   - Sources: Urea, Ammonium sulfate, DAP, CAN

2. Phosphorus (P):
   - Role: Root development, flowering, fruiting, energy transfer
   - Deficiency: Purple/dark green leaves, poor root growth, delayed maturity
   - Excess: Rare, may interfere with zinc uptake
   - Sources: DAP, SSP, Rock phosphate

3. Potassium (K):
   - Role: Disease resistance, water regulation, grain quality
   - Deficiency: Scorched leaf margins, weak stems, poor grain filling
   - Excess: May interfere with calcium and magnesium uptake
   - Sources: MOP (Muriate of Potash), SOP (Sulfate of Potash)

Secondary Nutrients:
- Calcium (Ca): Cell wall strength, root hair development
- Magnesium (Mg): Central component of chlorophyll
- Sulfur (S): Protein synthesis, oil content in oilseeds

Micronutrients:
- Zinc (Zn): Enzyme activation, hormone production
- Iron (Fe): Chlorophyll synthesis
- Manganese (Mn): Photosynthesis
- Copper (Cu): Reproductive growth
- Boron (B): Flowering and fruiting
- Molybdenum (Mo): Nitrogen fixation in legumes

CROP-SPECIFIC FERTILIZER RECOMMENDATIONS

WHEAT (Irrigated):
General Recommendation per hectare:
- Nitrogen: 120-150 kg
- Phosphorus: 60-80 kg P2O5
- Potassium: 40-60 kg K2O
- Zinc: 25 kg ZnSO4 (if deficient)

Application Schedule:
1. Basal (at sowing):
   - 1/3 of Nitrogen (40-50 kg)
   - Full Phosphorus (60-80 kg)
   - Full Potassium (40-60 kg)
   - Full Zinc (if needed)

2. First Top Dressing (21 days after sowing - CRI stage):
   - 1/3 of Nitrogen (40-50 kg)

3. Second Top Dressing (40-45 days - tillering):
   - Remaining Nitrogen (40-50 kg)

For Rain-fed Wheat:
- Reduce nitrogen to 80-100 kg/ha
- Apply all at sowing or split into 2 doses

Soil-Specific Adjustments:
- Black Soil: Reduce phosphorus by 10-15%
- Sandy Soil: Increase potassium by 20-25%
- Saline Soil: Use gypsum and reduce nitrogen

RICE (PADDY):
General Recommendation per hectare:
- Nitrogen: 120-150 kg
- Phosphorus: 60 kg P2O5
- Potassium: 40 kg K2O
- Zinc: 25 kg ZnSO4

Application Schedule:
1. Basal (at transplanting):
   - 1/4 of Nitrogen (30-40 kg)
   - Full Phosphorus
   - Full Potassium
   - Full Zinc

2. Tillering Stage (20-25 days):
   - 1/2 of Nitrogen (60-75 kg)

3. Panicle Initiation (40-45 days):
   - Remaining Nitrogen (30-40 kg)

For Direct Seeded Rice:
- Apply basal dose 2-3 weeks after sowing
- Adjust timing based on crop growth

Special Considerations:
- Coastal saline areas: Add 25 kg ZnSO4 + 50 kg FeSO4
- Organic carbon <0.5%: Increase nitrogen by 10-15%

COTTON:
General Recommendation per hectare:
- Nitrogen: 120-150 kg
- Phosphorus: 60 kg P2O5
- Potassium: 60 kg K2O
- Sulfur: 40 kg
- Boron: 5 kg (critical)

Application Schedule:
1. Basal (at sowing):
   - 25% Nitrogen (30-40 kg)
   - Full Phosphorus
   - 50% Potassium (30 kg)

2. 30 Days After Sowing:
   - 25% Nitrogen (30-40 kg)

3. 60 Days (Square Formation):
   - 25% Nitrogen (30-40 kg)
   - 50% Potassium (30 kg)

4. 90 Days (Flowering):
   - 25% Nitrogen (30-40 kg)
   - Foliar spray of 0.2% Boron

For Bt Cotton:
- Increase nitrogen by 10-15%
- More potassium for better boll development

SOYBEAN:
General Recommendation per hectare:
- Nitrogen: 20-30 kg (reduces with good Rhizobium inoculation)
- Phosphorus: 60-80 kg P2O5 (critical)
- Potassium: 30-40 kg K2O
- Sulfur: 20-30 kg
- Molybdenum: Seed treatment

Application Method:
- All nutrients at sowing (band placement)
- Seed treatment with Rhizobium + PSB
- Foliar spray of 2% DAP at flowering if needed

Black Soil Adjustment:
- Reduce phosphorus by 10-15%
- Add 500 kg FYM per hectare

MAIZE:
General Recommendation per hectare:
- Nitrogen: 120-150 kg
- Phosphorus: 60-80 kg P2O5
- Potassium: 40-60 kg K2O
- Zinc: 25 kg ZnSO4

Application Schedule:
1. Basal:
   - 1/3 Nitrogen
   - Full Phosphorus
   - Full Potassium
   - Full Zinc

2. 30 Days (Knee-high stage):
   - 1/3 Nitrogen

3. 50 Days (Tasseling):
   - Remaining Nitrogen

SOIL TYPE-BASED MODIFICATIONS

Black Soil (Vertisols) - Maharashtra, MP, Gujarat:
Characteristics: High clay, moisture retention, rich in Ca and Mg
- Reduce phosphorus by 10-15%
- Normal nitrogen requirements
- Add zinc (often deficient)
- pH: 7.5-8.5 (slightly alkaline)

Alluvial Soil - Punjab, Haryana, UP, Bihar:
Characteristics: Good fertility, well-drained
- Standard NPK recommendations
- Monitor potassium (can be depleted)
- Good response to organic matter
- pH: 6.5-7.5 (neutral)

Red Soil - Karnataka, Tamil Nadu, AP:
Characteristics: Low fertility, acidic, poor water retention
- Increase nitrogen by 15-20%
- Increase phosphorus by 10-15%
- Add lime if pH <5.5
- Add organic matter for water retention
- pH: 5.0-6.5 (acidic)

Laterite Soil - Kerala, Coastal regions:
Characteristics: Highly leached, acidic, low fertility
- Increase all nutrients by 20-25%
- Add lime (500-1000 kg/ha)
- Heavy organic manure application
- Frequent split applications
- pH: 4.5-6.0 (acidic)

Sandy Soil - Rajasthan, parts of Gujarat:
Characteristics: Low water and nutrient retention
- Increase potassium by 25-30%
- Split nitrogen into 3-4 doses
- Add organic matter (5-10 tons FYM/ha)
- Frequent light irrigations

USING SATELLITE DATA FOR PRECISION FERTILIZATION

NDVI-Based Nitrogen Management:
1. Divide field into zones based on NDVI:
   - High NDVI (>0.7): Reduce nitrogen by 15-20%
   - Medium NDVI (0.5-0.7): Standard dose
   - Low NDVI (<0.5): Increase nitrogen by 15-20%

2. Variable Rate Application:
   - Use GPS-enabled equipment
   - Can save 20-30% fertilizer costs
   - Improves efficiency and reduces waste

Mid-Season Correction:
If NDVI at critical stage is:
- 0.2-0.4 for wheat (40 days): Apply 30 kg N/ha immediately
- 0.3-0.5 for rice (30 days): Apply 40 kg N/ha
- 0.4-0.6 for cotton (60 days): Apply 25 kg N/ha + foliar nutrition

ORGANIC AND BIO-FERTILIZERS

Farmyard Manure (FYM):
- Application rate: 10-15 tons/ha
- NPK equivalent: Approximately 0.5-0.5-0.5 per ton
- Apply 2-3 weeks before sowing
- Improves soil structure and water holding capacity

Vermicompost:
- Application rate: 5-7 tons/ha
- NPK equivalent: 1.5-1.5-1.5 per ton
- Rich in micronutrients and beneficial microbes
- Can be applied closer to sowing

Biofertilizers:
1. Rhizobium (for legumes): 200g per 10kg seed
2. Azotobacter (for cereals): 200g per 10kg seed
3. PSB - Phosphorus Solubilizing Bacteria: 200g per 10kg seed
4. Azospirillum: For rice, maize - 200g per 10kg seed

Green Manuring:
- Dhaincha, Sunhemp cultivation
- Incorporate 40-50 days after sowing
- Equivalent to 30-40 kg N/ha
- Improves soil health significantly

FERTIGATION (Fertilizer through Irrigation):

Advantages:
- Uniform distribution
- Higher efficiency (20-30% savings)
- Timely nutrition supply
- Suitable for drip and sprinkler systems

NPK Fertigation Schedule (General):
- Week 1-2: 10% of total
- Week 3-4: 20% of total
- Week 5-6: 30% of total
- Week 7-8: 25% of total
- Week 9-10: 15% of total

Soluble Fertilizers for Fertigation:
- Urea, Ammonium nitrate
- Mono Ammonium Phosphate (MAP)
- Potassium nitrate, Potassium sulfate
- Calcium nitrate
- Micronutrient chelates

FOLIAR NUTRITION

When to Use:
- Quick correction of deficiencies
- Critical growth stages
- Adverse soil conditions
- Supplement to soil application

Common Foliar Sprays:
1. 2% DAP spray: General nutrient boost
2. 1% Urea spray: Nitrogen deficiency
3. 0.5% MOP spray: Potassium deficiency
4. 0.5% Zinc sulfate: Zinc deficiency
5. 0.2% Boron: For cotton, oilseeds
6. 19:19:19 (NPK) spray: Balanced nutrition

Application Tips:
- Spray in early morning or evening
- Ensure good coverage
- Add wetting agent (0.1% Teepol)
- Repeat after 10-15 days if needed
- Avoid during flowering (for insect-pollinated crops)

COMMON MISTAKES TO AVOID

1. Excessive Nitrogen:
   - Causes lodging in cereals
   - Increases pest and disease susceptibility
   - Reduces grain quality
   - Pollution through leaching

2. Imbalanced Nutrition:
   - High N with low K: Weak plants, poor disease resistance
   - High P with low Zn: Zinc deficiency induced
   - Over-liming: Micronutrient deficiencies

3. Wrong Timing:
   - Late nitrogen application: Poor grain filling
   - Early application in sandy soil: Leaching losses
   - All nitrogen at once: Low efficiency

4. Poor Application Method:
   - Broadcasting urea on surface: 30-40% losses
   - Deep placement of phosphorus: Reduced availability
   - Not incorporating fertilizers: Volatilization losses

5. Ignoring Soil Testing:
   - Blanket recommendations may not suit your soil
   - Can lead to over or under-application"""