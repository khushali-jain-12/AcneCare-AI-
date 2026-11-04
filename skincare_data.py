"""
Skincare information and care recommendations for the 5 acne classes:
1. Blackheads (Open Comedones)
2. Whiteheads (Closed Comedones)
3. Papules (Inflammatory Bumps)
4. Pustules (Pus-filled Lesions)
5. Cyst (Deep Nodulocystic Acne)
"""

SKINCARE_GUIDE = {
    "Blackheads": {
        "title": "Blackheads (Open Comedones)",
        "category": "Non-Inflammatory Acne",
        "severity": "Mild",
        "badge_color": "#2D3748",
        "description": (
            "Blackheads occur when skin pores become clogged with excess sebum (oil) and "
            "dead skin cells. Unlike whiteheads, the pore opening remains open to air. "
            "Exposure to oxygen oxidizes melanin in the trapped debris, turning it dark brown or black—"
            "it is not trapped dirt."
        ),
        "primary_causes": [
            "Excess sebum (oil) production by overactive sebaceous glands",
            "Slow natural shedding of dead epidermal keratinocytes",
            "Hormonal fluctuations causing increased pore congestion",
            "Use of heavy, occlusive, or comedogenic cosmetic oils"
        ],
        "key_ingredients": [
            {
                "name": "Salicylic Acid (BHA 1-2%)",
                "purpose": "Oil-soluble acid that penetrates deep into pores to dissolve sebum plugs and exfoliate dead cells."
            },
            {
                "name": "Niacinamide (2-5%)",
                "purpose": "Regulates sebum production, strengthens skin barrier, and visibly tightens enlarged pores."
            },
            {
                "name": "Retinol / Adapalene",
                "purpose": "Accelerates cellular turnover, preventing future pore blockages from forming."
            },
            {
                "name": "Clay Masks (Kaolin / Bentonite)",
                "purpose": "Gently draws out surface impurities and controls mid-day shine without over-stripping."
            }
        ],
        "routine": {
            "morning": [
                "Gentle Gel Cleanser (fragrance-free, non-stripping)",
                "Hydrating Niacinamide Serum (helps balance oil flow)",
                "Lightweight, Oil-Free Gel Moisturizer",
                "Broad-Spectrum SPF 30+ Sunscreen (oil-free, non-comedogenic)"
            ],
            "evening": [
                "Gentle Cleanser (or double cleanse with micellar water)",
                "Salicylic Acid (BHA) Leave-on Exfoliant (2-3 nights/week)",
                "Barrier-Supporting Lightweight Ceramide Moisturizer"
            ]
        },
        "dos": [
            "Cleanse your face twice daily with lukewarm water.",
            "Use non-comedogenic and water-based skincare products.",
            "Wash pillowcases and clean your phone screen weekly to prevent bacteria transfer."
        ],
        "donts": [
            "Do NOT use metal comedone extractors or pinch blackheads with fingernails—it damages pore walls.",
            "Avoid pore strips frequently; they can cause capillary breakage and stretch pores.",
            "Avoid physical walnut/apricot face scrubs that cause micro-tears on sensitive skin."
        ],
        "when_to_see_doctor": (
            "Consult a board-certified dermatologist if over-the-counter BHA and retinoids do not show "
            "improvement after 8 to 12 weeks, or if pores frequently become inflamed into red papules."
        )
    },

    "Whiteheads": {
        "title": "Whiteheads (Closed Comedones)",
        "category": "Non-Inflammatory Acne",
        "severity": "Mild",
        "badge_color": "#4A5568",
        "description": (
            "Whiteheads are closed comedones that form when excess sebum and dead skin cells "
            "clog a microscopic hair follicle, but unlike blackheads, a microscopic layer of skin cells covers "
            "the pore opening. Because air cannot reach the trapped sebum, it remains pale white or flesh-colored."
        ),
        "primary_causes": [
            "Trapped sebum beneath an intact stratum corneum layer",
            "Elevated keratinization (abnormal buildup of surface skin cells)",
            "Hormonal shifts (puberty, menstrual cycle, androgenic hormones)",
            "Heavy or pore-clogging makeup, thick balms, and heavy sunscreens"
        ],
        "key_ingredients": [
            {
                "name": "Salicylic Acid (BHA)",
                "purpose": "Penetrates lipid-rich follicle walls to unclog trapped keratin and oil."
            },
            {
                "name": "Glycolic / Lactic Acid (AHA)",
                "purpose": "Water-soluble exfoliant that gently sweeps away surface skin cells covering the pore."
            },
            {
                "name": "Adapalene (0.1%) / Topical Retinoids",
                "purpose": "Gold standard for normalizing follicular keratinization and preventing comedones."
            },
            {
                "name": "Azelaic Acid (10%)",
                "purpose": "Provides dual exfoliation and antibacterial benefits while calming underlying redness."
            }
        ],
        "routine": {
            "morning": [
                "Gentle Foaming or Gel Cleanser",
                "Lightweight hydrating toner or hyaluronic acid essence",
                "Oil-Free Fluid Moisturizer with Hyaluronic Acid",
                "Matte-Finish Broad Spectrum SPF 50"
            ],
            "evening": [
                "Gentle Cleanser",
                "Topical Retinoid (Adapalene 0.1% or Retinol) applied to dry skin",
                "Hydrating, non-comedogenic ceramide lotion"
            ]
        },
        "dos": [
            "Introduce chemical exfoliants gradually (start 1-2 times weekly).",
            "Always patch-test new skincare actives on the inner forearm first.",
            "Look for 'non-comedogenic' and 'oil-free' labeling on all face products."
        ],
        "donts": [
            "Never squeeze or pop whiteheads; squeezing pushes the plug deeper and risks inflammatory cysts.",
            "Do not over-wash your face; cleansing more than twice daily triggers rebound oil production.",
            "Avoid heavy occlusives like petroleum jelly directly over comedone-prone areas."
        ],
        "when_to_see_doctor": (
            "If whiteheads are widespread, stubborn to topical retinoids after 8-10 weeks, or develop into "
            "inflamed red bumps, consult a dermatologist for prescription-strength topical therapies."
        )
    },

    "Papules": {
        "title": "Papules (Inflammatory Bumps)",
        "category": "Inflammatory Acne",
        "severity": "Moderate",
        "badge_color": "#E53E3E",
        "description": (
            "Papules are small, solid, raised pink or reddish bumps on the skin. They develop when "
            "a clogged pore becomes colonized by Cutibacterium acnes (C. acnes) bacteria, causing the follicular "
            "wall to rupture slightly and trigger localized inflammation in the surrounding dermis. "
            "They do not contain visible pus at the surface."
        ),
        "primary_causes": [
            "Rupture of the follicle wall due to pressure from trapped sebum and debris",
            "Proliferation of Cutibacterium acnes (formerly P. acnes) bacteria",
            "Localized immune response causing redness, swelling, and tenderness",
            "Friction from phone contact, helmets, pillowcases, or face-touching"
        ],
        "key_ingredients": [
            {
                "name": "Benzoyl Peroxide (2.5% - 5%)",
                "purpose": "Releases oxygen directly into pores to destroy anaerobic C. acnes bacteria quickly without resistance."
            },
            {
                "name": "Azelaic Acid (10% - 15%)",
                "purpose": "Potent anti-inflammatory agent that calms erythema (redness) and targets post-acne marks."
            },
            {
                "name": "Centella Asiatica (Cica) & Panthenol",
                "purpose": "Soothes irritated skin, accelerates healing, and reduces inflammatory swelling."
            },
            {
                "name": "Niacinamide (4%)",
                "purpose": "Inhibits pro-inflammatory cytokines, calming redness and strengthening compromised barrier."
            }
        ],
        "routine": {
            "morning": [
                "Gentle Hydrating Cleanser",
                "Calming Centella Asiatica / Niacinamide Serum",
                "Lightweight Soothing Moisturizer",
                "Mineral or Gentle Chemical Sunscreen (SPF 30+)"
            ],
            "evening": [
                "Gentle Cleanser",
                "Benzoyl Peroxide (2.5% wash or leave-on spot treatment on dry skin)",
                "Moisturizing Cream containing Ceramides and Squalane to counteract dryness"
            ]
        },
        "dos": [
            "Apply cold compresses wrapped in clean tissue for 5 minutes to reduce acute swelling and pain.",
            "Apply hydrocolloid pimple patches to protect inflamed bumps from unconscious picking.",
            "Use lower concentrations of Benzoyl Peroxide (2.5% is as effective as 10% with far less irritation)."
        ],
        "donts": [
            "NEVER attempt to pop a papule; there is no pus center, and squeezing causes deeper dermis damage and scarring.",
            "Do not scrub skin vigorously with abrasive cleansing brushes or loofahs.",
            "Avoid combining multiple strong drying treatments (e.g. BHA + high alcohol + benzoyl) simultaneously."
        ],
        "when_to_see_doctor": (
            "Seek a dermatologist's evaluation if papules are persistent, tender, spreading rapidly, or "
            "causing post-inflammatory hyperpigmentation or scarring."
        )
    },

    "Pustules": {
        "title": "Pustules (Pus-Filled Lesions)",
        "category": "Inflammatory Acne",
        "severity": "Moderate",
        "badge_color": "#DD6B20",
        "description": (
            "Pustules are classic inflamed blemishes with a defined, raised red ring around the base "
            "and a clearly visible white or yellowish center. The white core is formed by an accumulation "
            "of dead immune cells (leukocytes), cellular debris, and inflammatory fluid as the body fights off "
            "bacterial activity within the pore."
        ),
        "primary_causes": [
            "Severe inflammatory cascade within the sebaceous follicle",
            "Accumulation of white blood cells (neutrophils) combating bacteria",
            "Pore wall breakdown releasing bacteria into adjacent tissue",
            "Fluctuating androgen hormone levels stimulating high oil synthesis"
        ],
        "key_ingredients": [
            {
                "name": "Benzoyl Peroxide (2.5% - 4%)",
                "purpose": "Antibacterial action clears bacteria, dries excess pus, and halts new lesion growth."
            },
            {
                "name": "Hydrocolloid Acne Patches",
                "purpose": "Absorbs exudate/pus safely, keeps the lesion sterile, and physically prevents picking."
            },
            {
                "name": "Tea Tree Extract / Melaleuca (low %)",
                "purpose": "Natural antimicrobial properties that help reduce swelling and bacterial burden."
            },
            {
                "name": "Zinc PCA",
                "purpose": "Antimicrobial and astringent mineral that regulates sebum and calms angry redness."
            }
        ],
        "routine": {
            "morning": [
                "Gentle Foaming Cleanser (or 2% Salicylic Cleanser)",
                "Soothing Anti-Redness Serum (Centella, Green Tea, or Zinc)",
                "Light Gel-Cream Barrier Moisturizer",
                "Non-greasy, non-comedogenic Broad-Spectrum Sunscreen SPF 50"
            ],
            "evening": [
                "Gentle Purifying Cleanser (lukewarm water, pat dry with fresh towel)",
                "Hydrocolloid pimple patch directly over pustules (or localized Benzoyl Peroxide spot treatment)",
                "Gentle Barrier Support Cream (no active peeling agents on open lesions)"
            ]
        },
        "dos": [
            "Use clean hydrocolloid acne patches overnight to draw out fluid cleanly.",
            "Pat the face dry with a clean paper towel or freshly laundered washcloth.",
            "Keep hands strictly away from the face throughout the day."
        ],
        "donts": [
            "NEVER pop pustules with bare fingers; popping forces infectious bacteria deeper into healthy skin tissue.",
            "Avoid harsh physical astringents, 70% rubbing alcohol, or toothpaste on pustules.",
            "Do not pick off crusts or scabs while the lesion is healing."
        ],
        "when_to_see_doctor": (
            "If pustules occur in large clusters, are painful, or leave dark marks or indentations, consult "
            "a dermatologist for clinical topical formulations (e.g., Clindamycin + Benzoyl Peroxide) or oral treatments."
        )
    },

    "Cyst": {
        "title": "Cystic Acne (Nodulocystic Lesions)",
        "category": "Severe Inflammatory Acne",
        "severity": "Severe",
        "badge_color": "#9B2C2C",
        "description": (
            "Cystic acne is the most severe form of acne vulgaris. It presents as large, deep, painful, "
            "fluid-filled lumps that develop deep beneath the skin's surface. Cysts occur when a follicle wall ruptures "
            "deep within the dermis, causing a widespread inflammatory reaction. Cysts pose the highest risk of "
            "permanent atrophic (ice-pick, boxcar) scarring if not managed carefully."
        ),
        "primary_causes": [
            "Deep dermal follicular rupture triggering an intense local immune response",
            "Severe genetic predisposition and hormonal imbalances (high androgen sensitivity)",
            "Deep sebum retention combined with dense C. acnes colonization",
            "Excessive immune hypersensitivity to bacterial antigens"
        ],
        "key_ingredients": [
            {
                "name": "Oral / Prescription Retinoids (Isotretinoin)",
                "purpose": "Prescribed by dermatologists; the most effective systemic treatment for severe cystic acne."
            },
            {
                "name": "Topical Retinoids (Adapalene / Tretinoin)",
                "purpose": "Prescription topical treatments that normalize deep cellular turnover."
            },
            {
                "name": "Azelaic Acid (15% - 20%)",
                "purpose": "Deep anti-inflammatory and antibacterial agent that reduces pigmentation risk."
            },
            {
                "name": "Barrier Repair Ingredients (Ceramides, Hyaluronic Acid)",
                "purpose": "Crucial to maintain skin integrity and prevent flaking during medical treatments."
            }
        ],
        "routine": {
            "morning": [
                "Ultra-Gentle, Hydrating Non-Foaming Cleanser",
                "Centella Asiatica / Hyaluronic Acid hydrating serum",
                "Soothing, fragrance-free barrier repair cream",
                "High-protection Mineral Sunscreen SPF 50+ (Zinc Oxide is soothing to inflamed skin)"
            ],
            "evening": [
                "Gentle Cleanser (pat dry gently without rubbing)",
                "Dermatologist-prescribed treatment (or 10% Azelaic Acid / gentle OTC retinoid)",
                "Rich Ceramide Moisturizer to protect and soothe the skin barrier"
            ]
        },
        "dos": [
            "Schedule an appointment with a board-certified dermatologist for medical evaluation.",
            "Apply wrapped ice cubes for 5-10 minutes to relieve throbbing pain and swelling.",
            "Keep the skin consistently moisturized to aid the healing process."
        ],
        "donts": [
            "ABSOLUTELY NEVER attempt to squeeze, lance, or puncture a cyst—this causes severe dermal scarring and tissue necrosis.",
            "Do not overload skin with multiple harsh drugstore acne treatments; they cannot reach deep cysts and will only burn surface skin.",
            "Avoid hot water and aggressive face brushes."
        ],
        "when_to_see_doctor": (
            "Dermatologist consultation is STRONGLY RECOMMENDED for cystic acne. Over-the-counter products "
            "rarely penetrate deeply enough to resolve cystic lesions. In-office cortisone injections, prescription oral antibiotics, "
            "hormonal therapies, or oral isotretinoin can provide rapid relief and prevent permanent scarring."
        )
    }
}

# General holistic skincare tips applicable to all acne types
GENERAL_SKINCARE_PRINCIPLES = [
    {
        "title": "Gentle Cleansing Over Stripping",
        "description": "Washing with harsh, high-pH soaps damages the skin barrier and paradoxically causes skin to produce even more oil. Use a gentle, pH-balanced cleanser twice daily."
    },
    {
        "title": "Daily Sun Protection (SPF 30+)",
        "description": "UV radiation worsens post-inflammatory erythema (red marks) and post-inflammatory hyperpigmentation (dark spots). Always finish your morning routine with non-comedogenic sunscreen."
    },
    {
        "title": "Hydration is Essential",
        "description": "Oily or acne-prone skin still requires hydration. Dehydrated skin compromises the lipid barrier, making skin more susceptible to bacterial infection and irritation."
    },
    {
        "title": "Patience and Consistency",
        "description": "Acne treatments and retinoids typically require 6 to 12 weeks of consistent application before visible improvements appear, as the skin's turnover cycle takes 28 to 40 days."
    }
]

DISCLAIMER_TEXT = (
    "This web application is developed strictly as an academic project for an "
    "Artificial Neural Networks & Deep Learning coursework. The classification and information provided "
    "are for demonstration and educational purposes only. It is NOT intended as a clinical diagnosis, medical advice, "
    "or a substitute for professional dermatological consultation. Always seek the advice of a qualified healthcare "
    "provider for any skin condition."
)

