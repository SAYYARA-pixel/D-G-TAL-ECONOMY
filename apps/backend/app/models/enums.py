import enum


class RoleCode(str, enum.Enum):
    SUPER_ADMIN = 'super_admin'
    MINISTRY_ADMIN = 'ministry_admin'
    LEGAL_EXPERT = 'legal_expert'
    POLICY_ANALYST = 'policy_analyst'
    ANALYST_VIEWER = 'analyst_viewer'
    PUBLIC_USER = 'public_user'
    ENTREPRENEUR_USER = 'entrepreneur_user'


class FindingRisk(str, enum.Enum):
    LOW = 'low'
    MEDIUM = 'medium'
    HIGH = 'high'


class ReviewStatus(str, enum.Enum):
    DRAFT = 'draft'
    IN_REVIEW = 'in_review'
    RESOLVED = 'resolved'
