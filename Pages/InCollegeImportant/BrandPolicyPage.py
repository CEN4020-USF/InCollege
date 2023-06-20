import MainMenu as Menu
from Util import db_helper as db
from Pages import LoginPage
from Pages.Useful import GeneralPage as General

class BrandPolicyPage:

    def menu(self):

        brand_policy = """**InCollege Brand Usage Guidelines**

Welcome to the InCollege Brand Usage Guidelines. This document outlines the guidelines for using InCollege's brand assets to ensure consistent and accurate representation of our brand. These guidelines apply to both internal teams and external partners.

**1. InCollege Logo Usage:**

- Always use the approved InCollege logo downloaded from our official brand resources.
- Maintain the logo's proportions and clear space requirements. Do not alter, distort, or modify the logo in any way.
- Respect the logo's color variations. Use the full-color logo on light backgrounds and the white logo on dark backgrounds.
- Do not place the logo on visually cluttered or busy backgrounds that compromise its visibility and legibility.

**2. Color Palette:**

- Our primary color is InCollege Blue (#0077B5). Please use this color consistently in your communications.
- You may use secondary colors, such as gray (#F2F2F2) and black (#000000), to complement the primary color.
- Avoid using colors that conflict with our brand guidelines or create confusion about our identity.

**3. Typography:**

- Our official typeface is Arial. Please use Arial or Arial Bold for all InCollege-related text.
- Maintain appropriate font sizes, line heights, and spacing for optimal legibility across different mediums.
- Follow proper text hierarchy, using bold or italic styles sparingly for emphasis.

**4. Imagery and Photography:**

- Select images and photography that align with a professional and inclusive tone.
- Images should reflect diversity and inclusivity, representing various industries, professions, and demographics.
- Avoid using images that are overly staged or too casual, as they may not align with our brand positioning.

**5. Tone of Voice:**

- Use a professional and friendly tone in all written communications.
- Maintain a balance between being informative and approachable, without being overly formal or casual.
- Tailor the tone based on the context and target audience, but always reflect our brand values of professionalism and integrity.

**6. Iconography and Graphic Elements:**

- Use InCollege-approved icons and graphic elements for consistency across your designs.
- Icons should be clear, simple, and universally recognizable.
- Avoid using icons or graphic elements that may cause confusion or misinterpretation.

**7. Use in Different Media:**

- Adapt the brand assets to different media platforms while maintaining visual consistency.
- Ensure that the brand assets are appropriately sized and optimized for each medium.
- Follow the platform-specific guidelines when using InCollege assets on third-party platforms or integrations.

**8. Brand Partnerships:**

- Co-branding or partnerships involving the InCollege brand must be approved in advance.
- Follow the co-branding guidelines provided separately for such collaborations.
- Clearly define the roles and responsibilities of each partner to ensure consistent representation of both brands.

**9. Misuse and Violations:**

- Any unauthorized alteration, distortion, or misuse of InCollege brand assets is strictly prohibited.
- Violations may result in legal consequences, including the termination of partnerships or legal action.
- Report any misuse or violations of InCollege brand assets to our legal team immediately.

By adhering to these guidelines, you contribute to maintaining the integrity and consistency of the InCollege brand. For detailed brand assets and further information, please refer to our official InCollege Brand Resources page. 
        """

        print(brand_policy)
        choice = int(input("0.) Return to previous "))
        while True:
            if choice != 0:
                choice = int(input("\nInvalid input please select number next to navigation link: "))
            else:
                break
        if choice == 0:
            return
