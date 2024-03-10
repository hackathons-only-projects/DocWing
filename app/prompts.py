

SP='''
act like a nurse for a healthcare service called 'healthily'. keep your responses as short as possible. use the knowledge of available service provided. patients will be chatting with you providing you with their symptoms and talking about their problems. your main goal is to recommend the service they should use from the ones provided on the knowledge base.do not give medical advice. if not yet certain what service to recommend, ask more questions about the symptoms and the problem in general. 
The task is to create a flow which rebalances the asymmetry of knowledge between the patient and healthcare professionals, based on their symptoms and the services available (generalist vs specialist services - physiotherapy, mental health etc instead of a GP).

example recommendation: you should use Acne treatments service healthily provides, find it right here :https://www.livehealthily.com/health-library/,  this service can provide you with...
'''


AP='''

keep your responses as short as possible, concise and to the point.
focus on quickly identifying which service to recommend and understanding the symptoms quickly.
The users will be anxious, frustrated and dependent on healthcare professionals.
you need to explain the benefits of the service recommended  to the user once you do. only recommend from the services within the scope of the knowledge base provided.

'''


KB='''
Abortion: Abortion: We provide safe and confidential procedures for terminating pregnancies.#

Acne treatments: Acne treatments: Our dermatologists offer various treatments to help you manage and clear your acne.#

Acupuncture: Acupuncture: Experience the ancient practice of acupuncture to address a wide range of health concerns, from pain management to stress relief.#

Adenoidectomy: Adenoidectomy: Surgical removal of the adenoids to improve breathing and alleviate recurrent infections.#

Amputation: Amputation: Surgical removal of a limb due to injury, disease, or medical necessity.#

Anaesthesia: Anaesthesia: Safe administration of medications to induce temporary loss of sensation or consciousness during medical procedures.#

Anger management: Anger management: Learn effective techniques to manage and control anger in healthy and constructive ways.#

Antidepressants: Antidepressants: Medications prescribed to alleviate symptoms of depression and improve overall mood.#

Antifungal medication: Antifungal medication: Treat fungal infections with our range of effective antifungal medications.#

Aortic valve replacement: Aortic valve replacement: Surgical procedure to replace a damaged or diseased aortic valve with a prosthetic valve.#

Arthroscopy: Arthroscopy: Minimally invasive surgical procedure to diagnose and treat joint problems using a small camera and specialized instruments.#

Artificial insemination: Artificial insemination: Assisted reproductive technique that involves the direct insertion of sperm into a woman's uterus to facilitate fertilization.#

Biopsy: Biopsy: Removal and examination of tissue samples for diagnostic purposes to determine the presence of disease.#

Blood transfusion: Blood transfusion: Safe transfer of blood or blood products from a donor to a recipient to replace lost blood or treat certain medical conditions.#

Bone marrow donation: Bone marrow donation: Voluntary donation of bone marrow to help patients with blood disorders or cancer.#

Bone marrow transplant: Bone marrow transplant: Procedure to replace damaged or diseased bone marrow with healthy marrow stem cells.#

Braces: Braces: Orthodontic devices used to straighten and align teeth for improved dental health and aesthetics.#

Breast implants: Breast implants: Surgical procedure to enhance breast size and shape using silicone or saline implants.#

Breast implants (PIP): Breast implants (PIP): Information on breast implants manufactured by Poly Implant Prothèse (PIP), including safety concerns and removal procedures.#

Breast reconstruction: Breast reconstruction: Surgical procedure to restore the shape and appearance of the breast following mastectomy or injury.#

Breast reduction: Breast reduction: Surgical procedure to reduce the size and reshape the breasts for improved comfort and aesthetics.#

Carotid endarterectomy: Carotid endarterectomy: Surgical procedure to remove plaque buildup from the carotid arteries to reduce the risk of stroke.#

Cataract surgery: Cataract surgery: Surgical removal of a cloudy lens from the eye and replacement with an artificial lens to restore vision.#

Chemotherapy: Chemotherapy: Treatment using powerful medications to destroy cancer cells or prevent their growth and spread.#

Circumcision: Circumcision: Surgical removal of the foreskin of the penis for medical, cultural, or religious reasons.#

Circumcision (children): Circumcision (children): Information on circumcision procedures for infants and young boys, including benefits and risks.#

Colostomy: Colostomy: Surgical procedure to create an opening in the abdominal wall to divert the flow of feces from the colon to a stoma bag.#

Cognitive behavioural therapy: Cognitive behavioural therapy: Psychotherapeutic approach that helps individuals identify and change negative thought patterns and behaviours to improve mental health.#

Cornea transplant: Cornea transplant: Surgical procedure to replace a damaged or diseased cornea with healthy donor tissue to restore vision.#

Coronary angioplasty: Coronary angioplasty: Minimally invasive procedure to widen narrowed or blocked coronary arteries and improve blood flow to the heart.#

Coronary artery bypass graft: Coronary artery bypass graft: Surgical procedure to reroute blood flow around blocked coronary arteries using healthy blood vessels.#

Cosmetic surgery: Cosmetic surgery: Surgical procedures aimed at enhancing physical appearance and improving self-confidence.#

Cosmetics (non-surgical): Cosmetics (non-surgical): Non-invasive treatments such as botox, fillers, and chemical peels to rejuvenate the skin and reduce signs of aging.#

Counselling: Counselling: Confidential support and guidance from trained professionals to help individuals cope with emotional difficulties and life challenges.#

Dental treatments: Dental treatments: Comprehensive dental care including preventive, restorative, and cosmetic treatments to maintain oral health and improve smiles.#

Dentures: Dentures: Removable prosthetic devices used to replace missing teeth and restore chewing function and facial aesthetics.#

Dialysis: Dialysis: Life-sustaining treatment for individuals with kidney failure, involving the removal of waste products and excess fluids from the blood.#

Dilatation and curettage (D&C): Dilatation and curettage (D&C): Surgical procedure to remove tissue from the uterus for diagnostic or therapeutic purposes.#

Drug addiction treatment: Drug addiction treatment: Comprehensive programs and therapies to help individuals overcome substance abuse and achieve long-term recovery.#

Ear correction (otoplasty): Ear correction (otoplasty): Surgical procedure to reshape and reposition protruding or misshapen ears for improved appearance.#

Eczema treatments: Eczema treatments: Management strategies and medications to alleviate symptoms of eczema and prevent flare-ups.#

Emollients: Emollients: Moisturizing creams and ointments to hydrate and soothe dry, itchy skin associated with various skin conditions.#

Gallbladder removal: Gallbladder removal: Surgical procedure to remove the gallbladder to treat gallstones and alleviate related symptoms.#

Gastrectomy: Gastrectomy: Surgical removal of part or all of the stomach to treat conditions such as stomach cancer or severe ulcers.#

Hair removal: Hair removal: Various methods for removing unwanted hair from different parts of the body, including shaving, waxing, and laser treatments.#

Hand tendon repair: Hand tendon repair: Surgical procedure to repair damaged or severed tendons in the hand to restore function and mobility.#

Hearing aids: Hearing aids: Assistive devices worn in or behind the ear to amplify sound and improve hearing for individuals with hearing loss.#

Heart transplant: Heart transplant: Surgical procedure to replace a damaged or failing heart with a healthy donor heart.#

Heart-lung transplant: Heart-lung transplant: Surgical procedure to replace both the heart and lungs in patients with severe heart and lung diseases.#

Hip replacement: Hip replacement: Surgical procedure to replace a damaged or diseased hip joint with an artificial implant to relieve pain and improve mobility.#

Home oxygen treatment: Home oxygen treatment: Provision of supplemental oxygen therapy for individuals with respiratory conditions to improve breathing and quality of life.#

Homeopathy: Homeopathy: Alternative medical system based on the concept of treating "like with like" using highly diluted natural substances to stimulate the body's healing processes.#

Hormone replacement therapy: Hormone replacement therapy: Treatment to supplement deficient hormones in the body, often used to manage symptoms of menopause or hormone-related conditions.#

How to get rid of a headache: How to get rid of a headache: Tips and strategies for relieving headaches and migraines through lifestyle changes, relaxation techniques, and medication.#

Hypnotherapy: Hypnotherapy: Therapeutic technique that uses hypnosis to induce a state of deep relaxation and heightened suggestibility to facilitate behavioral change and symptom relief.#

Hysterectomy: Hysterectomy: Surgical removal of the uterus to treat conditions such as uterine fibroids, endometriosis, or cancer.#

Ileostomy: Ileostomy: Surgical procedure to create an opening in the abdominal wall to divert the flow of feces from the small intestine to a stoma bag.#

Immunotherapy for allergies: Immunotherapy for allergies: Treatment that desensitizes the immune system to specific allergens, reducing the severity of allergic reactions over time.#

Infertility treatment: Infertility treatment: Assisted reproductive techniques such as in vitro fertilization (IVF) and intrauterine insemination (IUI) to help couples conceive.#

Inguinal hernia treatment: Inguinal hernia treatment: Surgical repair of a hernia that protrudes through the inguinal canal in the groin area.#

Intensive care: Intensive care: Specialized medical care for critically ill patients requiring close monitoring and advanced life support interventions.#

IVF: IVF: In vitro fertilization: Assisted reproductive technique involving the fertilization of eggs with sperm outside the body, followed by embryo transfer into the uterus.#

Kidney transplant: Kidney transplant: Surgical procedure to replace a failed or diseased kidney with a healthy donor kidney.#

Knee ligament surgery: Knee ligament surgery: Surgical repair or reconstruction of torn or damaged ligaments in the knee to restore stability and function.#

Knee replacement: Knee replacement: Surgical procedure to replace a damaged or diseased knee joint with an artificial implant to relieve pain and improve mobility.#

Labiaplasty: Labiaplasty: Surgical procedure to reshape and reduce the size of the labia minora for aesthetic or functional purposes.#

Laser eye surgery: Laser eye surgery: Refractive surgical procedures such as LASIK or PRK to correct vision problems and reduce dependence on glasses or contact lenses.#

Laxatives: Laxatives: Medications or substances used to promote bowel movements and relieve constipation.#

Liposuction: Liposuction: Surgical procedure to remove excess fat deposits from specific areas of the body to improve contours and proportions.#

Liver transplant: Liver transplant: Surgical procedure to replace a damaged or failing liver with a healthy donor liver.#

Local anaesthetic: Local anaesthetic: Medication used to numb a specific area of the body for minor surgical procedures or pain management.#

Long COVID treatment: Long COVID treatment: Comprehensive care and support for individuals experiencing persistent symptoms following a COVID-19 infection.#

Lumbar decompressive surgery: Lumbar decompressive surgery: Surgical procedure to relieve pressure on the spinal nerves in the lower back by removing part of the vertebral bone or disc.#

Lung transplant: Lung transplant: Surgical procedure to replace one or both diseased lungs with healthy donor lungs to improve breathing and quality of life.#

Mastectomy: Mastectomy: Surgical removal of one or both breasts to treat or prevent breast cancer.#

Menopause magnets: Menopause magnets: Alternative therapy using magnets to alleviate symptoms of menopause such as hot flashes and night sweats.#

Mental health therapy: Mental health therapy: Psychotherapy and counseling services to address a wide range of mental health issues and improve overall well-being.#

Migraine treatments: Migraine treatments: Medications and therapies to prevent and alleviate the symptoms of migraines, including pain relief and lifestyle changes.#

Mirena coil for Menopause: Mirena coil for Menopause: Information on the use of the Mirena intrauterine device (IUD) for managing symptoms of menopause and contraception.#

Occupational therapy: Occupational therapy: Therapeutic interventions to help individuals with physical, cognitive, or emotional challenges achieve greater independence and function in daily life.#

Organ donation: Organ donation: Voluntary donation of organs or tissues from deceased or living donors to save or improve the lives of others.#

Orthodontics: Orthodontics: Dental specialty focused on diagnosing, preventing, and correcting misaligned teeth and jaws using braces, aligners, and other appliances.#

Orthopaedic surgery: Orthopaedic surgery: Surgical procedures to treat musculoskeletal conditions and injuries, including fractures, arthritis, and sports injuries.#

Osteopathy: Osteopathy: Holistic approach to healthcare that emphasizes the interrelationship between the body's structure and function for optimal health and well-being.#

Pacemaker implantation: Pacemaker implantation: Surgical procedure to implant a small electronic device that regulates the heart's rhythm and prevents abnormal heartbeats.#

Painkillers: Painkillers: Medications used to relieve pain and discomfort, ranging from over-the-counter analgesics to prescription opioids.#

Pancreas transplant: Pancreas transplant: Surgical procedure to replace a diseased or malfunctioning pancreas with a healthy donor pancreas to treat diabetes.#

Penis enlargement: Penis enlargement: Surgical procedures and techniques to increase the size or girth of the penis for aesthetic or functional purposes.#

Photodynamic therapy (PDT): Photodynamic therapy (PDT): Treatment that uses light-sensitive drugs and a specific type of light to destroy abnormal cells or tissues.#

Physiotherapy: Physiotherapy: Rehabilitation treatment aimed at restoring movement and function following injury, surgery, or illness through exercise, manual therapy, and other modalities.#

Placebo effect: Placebo effect: Phenomenon in which a placebo, or inactive substance, produces a therapeutic effect due to the patient's belief in its efficacy.#

Plasma products: Plasma products: Blood products derived from donated plasma used to treat various medical conditions, including clotting disorders and immune deficiencies.#

Plastic surgery: Plastic surgery: Surgical specialty focused on reconstructing or enhancing facial and body features for aesthetic or functional purposes.#

Psychiatry: Psychiatry: Medical specialty focused on diagnosing, treating, and preventing mental, emotional, and behavioral disorders through medication, psychotherapy, and other interventions.#

Psychotherapy: Psychotherapy: Therapeutic approach that involves talking with a trained therapist to explore and resolve psychological issues, improve coping skills, and promote personal growth.#

Radiotherapy: Radiotherapy: Treatment using high-energy radiation to target and destroy cancer cells while minimizing damage to surrounding healthy tissue.#

Rape and sexual assault support: Rape and sexual assault support: Confidential support services for individuals who have experienced sexual violence, including counseling, advocacy, and resources.#

Rheumatoid arthritis treatment: Rheumatoid arthritis treatment: Comprehensive management strategies to control symptoms and slow the progression of rheumatoid arthritis, including medications, physical therapy, and lifestyle changes.#

Root canal treatment: Root canal treatment: Endodontic procedure to remove infected or damaged pulp from the tooth and seal the root canal to prevent further infection.#

Skin glue: Skin glue: Medical adhesive used to close wounds and incisions instead of traditional sutures or staples.#

Small bowel transplant: Small bowel transplant: Surgical procedure to replace a damaged or diseased small intestine with a healthy donor intestine to restore digestive function.#

Smoking treatments: Smoking treatments: Behavioral interventions, medications, and support services to help individuals quit smoking and overcome nicotine addiction.#

Steroid creams: Steroid creams: Topical medications containing corticosteroids to reduce inflammation and relieve itching, redness, and swelling associated with various skin conditions.#

Steroid injections: Steroid injections: Injections of corticosteroid medications to reduce inflammation and relieve pain in joints, muscles, and soft tissues.#

Teeth whitening: Teeth whitening: Cosmetic dental procedure to lighten and brighten teeth for a whiter, more radiant smile.#

TENS machine: TENS machine: Transcutaneous electrical nerve stimulation (TENS) therapy for pain relief using small electrical impulses delivered through electrodes placed on the skin.#

Tetanus vaccine: Tetanus vaccine: Immunization to prevent tetanus, a serious bacterial infection that affects the nervous system and can lead to muscle stiffness and spasms.#

Thyroid treatment (overactive): Thyroid treatment (overactive): Medications, radioactive iodine therapy, or surgery to reduce thyroid hormone production in individuals with an overactive thyroid gland.#

Thyroid treatment (underactive): Thyroid treatment (underactive): Replacement therapy with synthetic thyroid hormones to supplement deficient thyroid function in individuals with an underactive thyroid gland.#

Tracheostomy: Tracheostomy: Surgical procedure to create an opening in the windpipe (trachea) to bypass upper airway obstruction or facilitate long-term mechanical ventilation.#

Traction: Traction: Application of a continuous pulling force to bones or muscles to align fractured or dislocated bones, relieve pressure, or correct deformities.#

Treatment for fibromyalgia: all you need to know: Treatment for fibromyalgia: all you need to know: Comprehensive information on available treatments and management strategies for fibromyalgia, a chronic pain condition.#

TURP (prostate): TURP (prostate): Transurethral resection of the prostate (TURP): Surgical procedure to relieve urinary symptoms caused by an enlarged prostate gland.#

Urinary catheterisation: Urinary catheterisation: Insertion of a thin tube (catheter) into the bladder to drain urine, often used in medical settings or for individuals with urinary retention.#

Vasectomy: Vasectomy: Surgical procedure for male sterilization by cutting or blocking the vas deferens to prevent the release of sperm during ejaculation.#

Weight loss surgery: Weight loss surgery: Surgical procedures such as gastric bypass or gastric sleeve to help individuals achieve significant and sustainable weight loss.#

Wisdom tooth removal: Wisdom tooth removal: Surgical extraction of impacted or problematic wisdom teeth to alleviate pain and prevent dental complications.#

Weight loss injections – all you need to know: Weight loss injections – all you need to know: Information on injectable medications or supplements used for weight loss, including benefits, risks, and effectiveness.#

Your asthma action plan - prevent and treat asthma attacks: Your asthma action plan - prevent and treat asthma attacks: Personalized guidelines and strategies for managing asthma symptoms and preventing asthma attacks.#

'''


