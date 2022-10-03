from tmp.types.AbstractPlayerSearchInformation import AbstractPlayerSearchInformation
from tmp.types.AccountTagInformation import AccountTagInformation
from tmp.types.PlayerSearchCharacterNameInformation import PlayerSearchCharacterNameInformation
from tmp.types.PlayerSearchTagInformation import PlayerSearchTagInformation
from tmp.types.StatisticData import StatisticData
from tmp.types.StatisticDataBoolean import StatisticDataBoolean
from tmp.types.StatisticDataByte import StatisticDataByte
from tmp.types.StatisticDataInt import StatisticDataInt
from tmp.types.StatisticDataShort import StatisticDataShort
from tmp.types.StatisticDataString import StatisticDataString
from tmp.types.GameServerInformations import GameServerInformations
from tmp.types.Achievement import Achievement
from tmp.types.AchievementAchieved import AchievementAchieved
from tmp.types.AchievementAchievedRewardable import AchievementAchievedRewardable
from tmp.types.AchievementObjective import AchievementObjective
from tmp.types.AchievementStartedObjective import AchievementStartedObjective
from tmp.types.FightDispellableEffectExtendedInformations import FightDispellableEffectExtendedInformations
from tmp.types.AbstractFightDispellableEffect import AbstractFightDispellableEffect
from tmp.types.FightTemporaryBoostEffect import FightTemporaryBoostEffect
from tmp.types.FightTemporaryBoostStateEffect import FightTemporaryBoostStateEffect
from tmp.types.FightTemporaryBoostWeaponDamagesEffect import FightTemporaryBoostWeaponDamagesEffect
from tmp.types.FightTemporarySpellBoostEffect import FightTemporarySpellBoostEffect
from tmp.types.FightTemporarySpellImmunityEffect import FightTemporarySpellImmunityEffect
from tmp.types.FightTriggeredEffect import FightTriggeredEffect
from tmp.types.GameActionMark import GameActionMark
from tmp.types.GameActionMarkedCell import GameActionMarkedCell
from tmp.types.ServerSessionConstant import ServerSessionConstant
from tmp.types.ServerSessionConstantInteger import ServerSessionConstantInteger
from tmp.types.ServerSessionConstantLong import ServerSessionConstantLong
from tmp.types.ServerSessionConstantString import ServerSessionConstantString
from tmp.types.AbstractCharacterInformation import AbstractCharacterInformation
from tmp.types.CharacterBasicMinimalInformations import CharacterBasicMinimalInformations
from tmp.types.CharacterMinimalAllianceInformations import CharacterMinimalAllianceInformations
from tmp.types.CharacterMinimalGuildInformations import CharacterMinimalGuildInformations
from tmp.types.CharacterMinimalGuildPublicInformations import CharacterMinimalGuildPublicInformations
from tmp.types.CharacterMinimalInformations import CharacterMinimalInformations
from tmp.types.CharacterMinimalPlusLookAndGradeInformations import CharacterMinimalPlusLookAndGradeInformations
from tmp.types.CharacterMinimalPlusLookInformations import CharacterMinimalPlusLookInformations
from tmp.types.ActorAlignmentInformations import ActorAlignmentInformations
from tmp.types.ActorExtendedAlignmentInformations import ActorExtendedAlignmentInformations
from tmp.types.AlterationInfo import AlterationInfo
from tmp.types.CharacterCharacteristic import CharacterCharacteristic
from tmp.types.CharacterCharacteristicDetailed import CharacterCharacteristicDetailed
from tmp.types.CharacterCharacteristics import CharacterCharacteristics
from tmp.types.CharacterCharacteristicsInformations import CharacterCharacteristicsInformations
from tmp.types.CharacterCharacteristicValue import CharacterCharacteristicValue
from tmp.types.CharacterSpellModification import CharacterSpellModification
from tmp.types.CharacterUsableCharacteristicDetailed import CharacterUsableCharacteristicDetailed
from tmp.types.CharacterBaseInformations import CharacterBaseInformations
from tmp.types.CharacterHardcoreOrEpicInformations import CharacterHardcoreOrEpicInformations
from tmp.types.CharacterRemodelingInformation import CharacterRemodelingInformation
from tmp.types.CharacterToRemodelInformations import CharacterToRemodelInformations
from tmp.types.RemodelingInformation import RemodelingInformation
from tmp.types.DebtInformation import DebtInformation
from tmp.types.KamaDebtInformation import KamaDebtInformation
from tmp.types.PlayerNote import PlayerNote
from tmp.types.ActorRestrictionsInformations import ActorRestrictionsInformations
from tmp.types.PlayerStatus import PlayerStatus
from tmp.types.PlayerStatusExtended import PlayerStatusExtended
from tmp.types.ActorOrientation import ActorOrientation
from tmp.types.EntityDispositionInformations import EntityDispositionInformations
from tmp.types.EntityMovementInformations import EntityMovementInformations
from tmp.types.FightEntityDispositionInformations import FightEntityDispositionInformations
from tmp.types.GameContextActorInformations import GameContextActorInformations
from tmp.types.GameContextActorPositionInformations import GameContextActorPositionInformations
from tmp.types.GameRolePlayTaxCollectorInformations import GameRolePlayTaxCollectorInformations
from tmp.types.IdentifiedEntityDispositionInformations import IdentifiedEntityDispositionInformations
from tmp.types.MapCoordinates import MapCoordinates
from tmp.types.MapCoordinatesAndId import MapCoordinatesAndId
from tmp.types.MapCoordinatesExtended import MapCoordinatesExtended
from tmp.types.TaxCollectorStaticExtendedInformations import TaxCollectorStaticExtendedInformations
from tmp.types.TaxCollectorStaticInformations import TaxCollectorStaticInformations
from tmp.types.AbstractFightTeamInformations import AbstractFightTeamInformations
from tmp.types.BaseSpawnMonsterInformation import BaseSpawnMonsterInformation
from tmp.types.FightAllianceTeamInformations import FightAllianceTeamInformations
from tmp.types.FightCommonInformations import FightCommonInformations
from tmp.types.FightExternalInformations import FightExternalInformations
from tmp.types.FightLoot import FightLoot
from tmp.types.FightLootObject import FightLootObject
from tmp.types.FightOptionsInformations import FightOptionsInformations
from tmp.types.FightResultAdditionalData import FightResultAdditionalData
from tmp.types.FightResultExperienceData import FightResultExperienceData
from tmp.types.FightResultFighterListEntry import FightResultFighterListEntry
from tmp.types.FightResultListEntry import FightResultListEntry
from tmp.types.FightResultMutantListEntry import FightResultMutantListEntry
from tmp.types.FightResultPlayerListEntry import FightResultPlayerListEntry
from tmp.types.FightResultPvpData import FightResultPvpData
from tmp.types.FightResultTaxCollectorListEntry import FightResultTaxCollectorListEntry
from tmp.types.FightStartingPositions import FightStartingPositions
from tmp.types.FightTeamInformations import FightTeamInformations
from tmp.types.FightTeamLightInformations import FightTeamLightInformations
from tmp.types.FightTeamMemberCharacterInformations import FightTeamMemberCharacterInformations
from tmp.types.FightTeamMemberEntityInformation import FightTeamMemberEntityInformation
from tmp.types.FightTeamMemberInformations import FightTeamMemberInformations
from tmp.types.FightTeamMemberMonsterInformations import FightTeamMemberMonsterInformations
from tmp.types.FightTeamMemberTaxCollectorInformations import FightTeamMemberTaxCollectorInformations
from tmp.types.FightTeamMemberWithAllianceCharacterInformations import FightTeamMemberWithAllianceCharacterInformations
from tmp.types.GameContextBasicSpawnInformation import GameContextBasicSpawnInformation
from tmp.types.GameContextSummonsInformation import GameContextSummonsInformation
from tmp.types.GameFightAIInformations import GameFightAIInformations
from tmp.types.GameFightCharacterInformations import GameFightCharacterInformations
from tmp.types.GameFightCharacteristics import GameFightCharacteristics
from tmp.types.GameFightEffectTriggerCount import GameFightEffectTriggerCount
from tmp.types.GameFightEntityInformation import GameFightEntityInformation
from tmp.types.GameFightFighterEntityLightInformation import GameFightFighterEntityLightInformation
from tmp.types.GameFightFighterInformations import GameFightFighterInformations
from tmp.types.GameFightFighterLightInformations import GameFightFighterLightInformations
from tmp.types.GameFightFighterMonsterLightInformations import GameFightFighterMonsterLightInformations
from tmp.types.GameFightFighterNamedInformations import GameFightFighterNamedInformations
from tmp.types.GameFightFighterNamedLightInformations import GameFightFighterNamedLightInformations
from tmp.types.GameFightFighterTaxCollectorLightInformations import GameFightFighterTaxCollectorLightInformations
from tmp.types.GameFightMonsterInformations import GameFightMonsterInformations
from tmp.types.GameFightMonsterWithAlignmentInformations import GameFightMonsterWithAlignmentInformations
from tmp.types.GameFightMutantInformations import GameFightMutantInformations
from tmp.types.GameFightResumeSlaveInfo import GameFightResumeSlaveInfo
from tmp.types.GameFightSpellCooldown import GameFightSpellCooldown
from tmp.types.GameFightTaxCollectorInformations import GameFightTaxCollectorInformations
from tmp.types.SpawnCharacterInformation import SpawnCharacterInformation
from tmp.types.SpawnCompanionInformation import SpawnCompanionInformation
from tmp.types.SpawnInformation import SpawnInformation
from tmp.types.SpawnMonsterInformation import SpawnMonsterInformation
from tmp.types.SpawnScaledMonsterInformation import SpawnScaledMonsterInformation
from tmp.types.AllianceInformations import AllianceInformations
from tmp.types.AlternativeMonstersInGroupLightInformations import AlternativeMonstersInGroupLightInformations
from tmp.types.AnomalySubareaInformation import AnomalySubareaInformation
from tmp.types.AtlasPointsInformations import AtlasPointsInformations
from tmp.types.BasicAllianceInformations import BasicAllianceInformations
from tmp.types.BasicGuildInformations import BasicGuildInformations
from tmp.types.BasicNamedAllianceInformations import BasicNamedAllianceInformations
from tmp.types.GameRolePlayActorInformations import GameRolePlayActorInformations
from tmp.types.GameRolePlayCharacterInformations import GameRolePlayCharacterInformations
from tmp.types.GameRolePlayGroupMonsterInformations import GameRolePlayGroupMonsterInformations
from tmp.types.GameRolePlayGroupMonsterWaveInformations import GameRolePlayGroupMonsterWaveInformations
from tmp.types.GameRolePlayHumanoidInformations import GameRolePlayHumanoidInformations
from tmp.types.GameRolePlayMerchantInformations import GameRolePlayMerchantInformations
from tmp.types.GameRolePlayMountInformations import GameRolePlayMountInformations
from tmp.types.GameRolePlayMutantInformations import GameRolePlayMutantInformations
from tmp.types.GameRolePlayNamedActorInformations import GameRolePlayNamedActorInformations
from tmp.types.GameRolePlayNpcInformations import GameRolePlayNpcInformations
from tmp.types.GameRolePlayNpcWithQuestInformations import GameRolePlayNpcWithQuestInformations
from tmp.types.GameRolePlayPortalInformations import GameRolePlayPortalInformations
from tmp.types.GameRolePlayPrismInformations import GameRolePlayPrismInformations
from tmp.types.GameRolePlayTreasureHintInformations import GameRolePlayTreasureHintInformations
from tmp.types.GroupMonsterStaticInformations import GroupMonsterStaticInformations
from tmp.types.GroupMonsterStaticInformationsWithAlternatives import GroupMonsterStaticInformationsWithAlternatives
from tmp.types.GuildInAllianceInformations import GuildInAllianceInformations
from tmp.types.GuildInformations import GuildInformations
from tmp.types.HumanInformations import HumanInformations
from tmp.types.HumanOption import HumanOption
from tmp.types.HumanOptionAlliance import HumanOptionAlliance
from tmp.types.HumanOptionEmote import HumanOptionEmote
from tmp.types.HumanOptionFollowers import HumanOptionFollowers
from tmp.types.HumanOptionGuild import HumanOptionGuild
from tmp.types.HumanOptionObjectUse import HumanOptionObjectUse
from tmp.types.HumanOptionOrnament import HumanOptionOrnament
from tmp.types.HumanOptionSkillUse import HumanOptionSkillUse
from tmp.types.HumanOptionSpeedMultiplier import HumanOptionSpeedMultiplier
from tmp.types.HumanOptionTitle import HumanOptionTitle
from tmp.types.MonsterBoosts import MonsterBoosts
from tmp.types.MonsterInGroupInformations import MonsterInGroupInformations
from tmp.types.MonsterInGroupLightInformations import MonsterInGroupLightInformations
from tmp.types.ObjectItemInRolePlay import ObjectItemInRolePlay
from tmp.types.AlignmentWarEffortInformation import AlignmentWarEffortInformation
from tmp.types.BreachBranch import BreachBranch
from tmp.types.BreachReward import BreachReward
from tmp.types.ExtendedBreachBranch import ExtendedBreachBranch
from tmp.types.ExtendedLockedBreachBranch import ExtendedLockedBreachBranch
from tmp.types.ArenaLeagueRanking import ArenaLeagueRanking
from tmp.types.ArenaRankInfos import ArenaRankInfos
from tmp.types.ArenaRanking import ArenaRanking
from tmp.types.LeagueFriendInformations import LeagueFriendInformations
from tmp.types.DecraftedItemStackInfo import DecraftedItemStackInfo
from tmp.types.JobBookSubscription import JobBookSubscription
from tmp.types.JobCrafterDirectoryEntryJobInfo import JobCrafterDirectoryEntryJobInfo
from tmp.types.JobCrafterDirectoryEntryPlayerInfo import JobCrafterDirectoryEntryPlayerInfo
from tmp.types.JobCrafterDirectoryListEntry import JobCrafterDirectoryListEntry
from tmp.types.JobCrafterDirectorySettings import JobCrafterDirectorySettings
from tmp.types.JobDescription import JobDescription
from tmp.types.JobExperience import JobExperience
from tmp.types.MapNpcQuestInfo import MapNpcQuestInfo
from tmp.types.DungeonPartyFinderPlayer import DungeonPartyFinderPlayer
from tmp.types.NamedPartyTeam import NamedPartyTeam
from tmp.types.NamedPartyTeamWithOutcome import NamedPartyTeamWithOutcome
from tmp.types.PartyGuestInformations import PartyGuestInformations
from tmp.types.PartyInvitationMemberInformations import PartyInvitationMemberInformations
from tmp.types.PartyMemberArenaInformations import PartyMemberArenaInformations
from tmp.types.PartyMemberGeoPosition import PartyMemberGeoPosition
from tmp.types.PartyMemberInformations import PartyMemberInformations
from tmp.types.PartyEntityBaseInformation import PartyEntityBaseInformation
from tmp.types.PartyEntityMemberInformation import PartyEntityMemberInformation
from tmp.types.GameRolePlayNpcQuestFlag import GameRolePlayNpcQuestFlag
from tmp.types.QuestActiveDetailedInformations import QuestActiveDetailedInformations
from tmp.types.QuestActiveInformations import QuestActiveInformations
from tmp.types.QuestObjectiveInformations import QuestObjectiveInformations
from tmp.types.QuestObjectiveInformationsWithCompletion import QuestObjectiveInformationsWithCompletion
from tmp.types.PortalInformation import PortalInformation
from tmp.types.TreasureHuntFlag import TreasureHuntFlag
from tmp.types.TreasureHuntStep import TreasureHuntStep
from tmp.types.TreasureHuntStepDig import TreasureHuntStepDig
from tmp.types.TreasureHuntStepFight import TreasureHuntStepFight
from tmp.types.TreasureHuntStepFollowDirection import TreasureHuntStepFollowDirection
from tmp.types.TreasureHuntStepFollowDirectionToHint import TreasureHuntStepFollowDirectionToHint
from tmp.types.TreasureHuntStepFollowDirectionToPOI import TreasureHuntStepFollowDirectionToPOI
from tmp.types.BidExchangerObjectInfo import BidExchangerObjectInfo
from tmp.types.ForgettableSpellItem import ForgettableSpellItem
from tmp.types.GoldItem import GoldItem
from tmp.types.Item import Item
from tmp.types.ObjectEffects import ObjectEffects
from tmp.types.ObjectItem import ObjectItem
from tmp.types.ObjectItemGenericQuantity import ObjectItemGenericQuantity
from tmp.types.ObjectItemInformationWithQuantity import ObjectItemInformationWithQuantity
from tmp.types.ObjectItemMinimalInformation import ObjectItemMinimalInformation
from tmp.types.ObjectItemNotInContainer import ObjectItemNotInContainer
from tmp.types.ObjectItemQuantity import ObjectItemQuantity
from tmp.types.ObjectItemQuantityPriceDateEffects import ObjectItemQuantityPriceDateEffects
from tmp.types.ObjectItemToSell import ObjectItemToSell
from tmp.types.ObjectItemToSellInBid import ObjectItemToSellInBid
from tmp.types.ObjectItemToSellInHumanVendorShop import ObjectItemToSellInHumanVendorShop
from tmp.types.ObjectItemToSellInNpcShop import ObjectItemToSellInNpcShop
from tmp.types.SellerBuyerDescriptor import SellerBuyerDescriptor
from tmp.types.SpellItem import SpellItem
from tmp.types.ObjectEffect import ObjectEffect
from tmp.types.ObjectEffectCreature import ObjectEffectCreature
from tmp.types.ObjectEffectDate import ObjectEffectDate
from tmp.types.ObjectEffectDice import ObjectEffectDice
from tmp.types.ObjectEffectDuration import ObjectEffectDuration
from tmp.types.ObjectEffectInteger import ObjectEffectInteger
from tmp.types.ObjectEffectLadder import ObjectEffectLadder
from tmp.types.ObjectEffectMinMax import ObjectEffectMinMax
from tmp.types.ObjectEffectMount import ObjectEffectMount
from tmp.types.ObjectEffectString import ObjectEffectString
from tmp.types.EntityInformation import EntityInformation
from tmp.types.ProtectedEntityWaitingForHelpInfo import ProtectedEntityWaitingForHelpInfo
from tmp.types.FinishMoveInformations import FinishMoveInformations
from tmp.types.AbstractContactInformations import AbstractContactInformations
from tmp.types.AcquaintanceInformation import AcquaintanceInformation
from tmp.types.AcquaintanceOnlineInformation import AcquaintanceOnlineInformation
from tmp.types.FriendInformations import FriendInformations
from tmp.types.FriendOnlineInformations import FriendOnlineInformations
from tmp.types.FriendSpouseInformations import FriendSpouseInformations
from tmp.types.FriendSpouseOnlineInformations import FriendSpouseOnlineInformations
from tmp.types.IgnoredInformations import IgnoredInformations
from tmp.types.IgnoredOnlineInformations import IgnoredOnlineInformations
from tmp.types.Contribution import Contribution
from tmp.types.GuildEmblem import GuildEmblem
from tmp.types.GuildMember import GuildMember
from tmp.types.GuildRankInformation import GuildRankInformation
from tmp.types.GuildRankMinimalInformation import GuildRankMinimalInformation
from tmp.types.GuildRankPublicInformation import GuildRankPublicInformation
from tmp.types.HavenBagFurnitureInformation import HavenBagFurnitureInformation
from tmp.types.ApplicationPlayerInformation import ApplicationPlayerInformation
from tmp.types.GuildApplicationInformation import GuildApplicationInformation
from tmp.types.GuildLogbookEntryBasicInformation import GuildLogbookEntryBasicInformation
from tmp.types.GuildLogbookChestActivity import GuildLogbookChestActivity
from tmp.types.GuildLevelUpActivity import GuildLevelUpActivity
from tmp.types.GuildPaddockActivity import GuildPaddockActivity
from tmp.types.GuildPlayerFlowActivity import GuildPlayerFlowActivity
from tmp.types.GuildPlayerRankUpdateActivity import GuildPlayerRankUpdateActivity
from tmp.types.GuildRankActivity import GuildRankActivity
from tmp.types.GuildUnlockNewTabActivity import GuildUnlockNewTabActivity
from tmp.types.GuildRecruitmentInformation import GuildRecruitmentInformation
from tmp.types.AdditionalTaxCollectorInformations import AdditionalTaxCollectorInformations
from tmp.types.TaxCollectorBasicInformations import TaxCollectorBasicInformations
from tmp.types.TaxCollectorComplementaryInformations import TaxCollectorComplementaryInformations
from tmp.types.TaxCollectorFightersInformation import TaxCollectorFightersInformation
from tmp.types.TaxCollectorGuildInformations import TaxCollectorGuildInformations
from tmp.types.TaxCollectorInformations import TaxCollectorInformations
from tmp.types.TaxCollectorLootInformations import TaxCollectorLootInformations
from tmp.types.TaxCollectorMovement import TaxCollectorMovement
from tmp.types.TaxCollectorWaitingForHelpInformations import TaxCollectorWaitingForHelpInformations
from tmp.types.HavenBagRoomPreviewInformation import HavenBagRoomPreviewInformation
from tmp.types.AccountHouseInformations import AccountHouseInformations
from tmp.types.HouseGuildedInformations import HouseGuildedInformations
from tmp.types.HouseInformations import HouseInformations
from tmp.types.HouseInformationsForGuild import HouseInformationsForGuild
from tmp.types.HouseInformationsForSell import HouseInformationsForSell
from tmp.types.HouseInformationsInside import HouseInformationsInside
from tmp.types.HouseInstanceInformations import HouseInstanceInformations
from tmp.types.HouseOnMapInformations import HouseOnMapInformations
from tmp.types.Idol import Idol
from tmp.types.PartyIdol import PartyIdol
from tmp.types.InteractiveElement import InteractiveElement
from tmp.types.InteractiveElementNamedSkill import InteractiveElementNamedSkill
from tmp.types.InteractiveElementSkill import InteractiveElementSkill
from tmp.types.InteractiveElementWithAgeBonus import InteractiveElementWithAgeBonus
from tmp.types.MapObstacle import MapObstacle
from tmp.types.StatedElement import StatedElement
from tmp.types.SkillActionDescription import SkillActionDescription
from tmp.types.SkillActionDescriptionCollect import SkillActionDescriptionCollect
from tmp.types.SkillActionDescriptionCraft import SkillActionDescriptionCraft
from tmp.types.SkillActionDescriptionTimed import SkillActionDescriptionTimed
from tmp.types.TeleportDestination import TeleportDestination
from tmp.types.StorageTabInformation import StorageTabInformation
from tmp.types.UpdatedStorageTabInformation import UpdatedStorageTabInformation
from tmp.types.RecycledItem import RecycledItem
from tmp.types.EntityLook import EntityLook
from tmp.types.IndexedEntityLook import IndexedEntityLook
from tmp.types.SubEntity import SubEntity
from tmp.types.ItemDurability import ItemDurability
from tmp.types.MountClientData import MountClientData
from tmp.types.UpdateMountBooleanCharacteristic import UpdateMountBooleanCharacteristic
from tmp.types.UpdateMountCharacteristic import UpdateMountCharacteristic
from tmp.types.UpdateMountIntegerCharacteristic import UpdateMountIntegerCharacteristic
from tmp.types.MountInformationsForPaddock import MountInformationsForPaddock
from tmp.types.PaddockBuyableInformations import PaddockBuyableInformations
from tmp.types.PaddockContentInformations import PaddockContentInformations
from tmp.types.PaddockGuildedInformations import PaddockGuildedInformations
from tmp.types.PaddockInformations import PaddockInformations
from tmp.types.PaddockInformationsForSell import PaddockInformationsForSell
from tmp.types.PaddockInstancesInformations import PaddockInstancesInformations
from tmp.types.PaddockItem import PaddockItem
from tmp.types.CharacterCharacteristicForPreset import CharacterCharacteristicForPreset
from tmp.types.EntitiesPreset import EntitiesPreset
from tmp.types.ForgettableSpellsPreset import ForgettableSpellsPreset
from tmp.types.FullStatsPreset import FullStatsPreset
from tmp.types.IconNamedPreset import IconNamedPreset
from tmp.types.IdolsPreset import IdolsPreset
from tmp.types.ItemForPreset import ItemForPreset
from tmp.types.ItemsPreset import ItemsPreset
from tmp.types.Preset import Preset
from tmp.types.PresetsContainerPreset import PresetsContainerPreset
from tmp.types.SimpleCharacterCharacteristicForPreset import SimpleCharacterCharacteristicForPreset
from tmp.types.SpellForPreset import SpellForPreset
from tmp.types.SpellsPreset import SpellsPreset
from tmp.types.StatsPreset import StatsPreset
from tmp.types.AllianceInsiderPrismInformation import AllianceInsiderPrismInformation
from tmp.types.AlliancePrismInformation import AlliancePrismInformation
from tmp.types.PrismFightersInformation import PrismFightersInformation
from tmp.types.PrismGeolocalizedInformation import PrismGeolocalizedInformation
from tmp.types.PrismInformation import PrismInformation
from tmp.types.PrismSubareaEmptyInfo import PrismSubareaEmptyInfo
from tmp.types.Shortcut import Shortcut
from tmp.types.ShortcutEmote import ShortcutEmote
from tmp.types.ShortcutEntitiesPreset import ShortcutEntitiesPreset
from tmp.types.ShortcutObject import ShortcutObject
from tmp.types.ShortcutObjectIdolsPreset import ShortcutObjectIdolsPreset
from tmp.types.ShortcutObjectItem import ShortcutObjectItem
from tmp.types.ShortcutObjectPreset import ShortcutObjectPreset
from tmp.types.ShortcutSmiley import ShortcutSmiley
from tmp.types.ShortcutSpell import ShortcutSpell
from tmp.types.AbstractSocialGroupInfos import AbstractSocialGroupInfos
from tmp.types.AlliancedGuildFactSheetInformations import AlliancedGuildFactSheetInformations
from tmp.types.AllianceFactSheetInformations import AllianceFactSheetInformations
from tmp.types.GuildFactSheetInformations import GuildFactSheetInformations
from tmp.types.GuildInAllianceVersatileInformations import GuildInAllianceVersatileInformations
from tmp.types.GuildInsiderFactSheetInformations import GuildInsiderFactSheetInformations
from tmp.types.GuildVersatileInformations import GuildVersatileInformations
from tmp.types.StartupActionAddObject import StartupActionAddObject
from tmp.types.TrustCertificate import TrustCertificate
from tmp.types.Version import Version
from tmp.types.BufferInformation import BufferInformation

id_class = {
   "3354": AbstractPlayerSearchInformation,
   "7861": AccountTagInformation,
   "3129": PlayerSearchCharacterNameInformation,
   "5463": PlayerSearchTagInformation,
   "3816": StatisticData,
   "8667": StatisticDataBoolean,
   "1264": StatisticDataByte,
   "6188": StatisticDataInt,
   "9644": StatisticDataShort,
   "9721": StatisticDataString,
   "7562": GameServerInformations,
   "8543": Achievement,
   "4559": AchievementAchieved,
   "6135": AchievementAchievedRewardable,
   "9536": AchievementObjective,
   "1120": AchievementStartedObjective,
   "9699": FightDispellableEffectExtendedInformations,
   "4443": AbstractFightDispellableEffect,
   "455": FightTemporaryBoostEffect,
   "9112": FightTemporaryBoostStateEffect,
   "5975": FightTemporaryBoostWeaponDamagesEffect,
   "2": FightTemporarySpellBoostEffect,
   "6345": FightTemporarySpellImmunityEffect,
   "8023": FightTriggeredEffect,
   "4268": GameActionMark,
   "8580": GameActionMarkedCell,
   "1030": ServerSessionConstant,
   "9087": ServerSessionConstantInteger,
   "1241": ServerSessionConstantLong,
   "89": ServerSessionConstantString,
   "4983": AbstractCharacterInformation,
   "840": CharacterBasicMinimalInformations,
   "7909": CharacterMinimalAllianceInformations,
   "1492": CharacterMinimalGuildInformations,
   "6496": CharacterMinimalGuildPublicInformations,
   "8205": CharacterMinimalInformations,
   "3999": CharacterMinimalPlusLookAndGradeInformations,
   "293": CharacterMinimalPlusLookInformations,
   "6870": ActorAlignmentInformations,
   "7926": ActorExtendedAlignmentInformations,
   "6503": AlterationInfo,
   "9991": CharacterCharacteristic,
   "9854": CharacterCharacteristicDetailed,
   "2462": CharacterCharacteristics,
   "7582": CharacterCharacteristicsInformations,
   "3823": CharacterCharacteristicValue,
   "8178": CharacterSpellModification,
   "6677": CharacterUsableCharacteristicDetailed,
   "8446": CharacterBaseInformations,
   "9829": CharacterHardcoreOrEpicInformations,
   "234": CharacterRemodelingInformation,
   "2055": CharacterToRemodelInformations,
   "4836": RemodelingInformation,
   "4146": DebtInformation,
   "9864": KamaDebtInformation,
   "1005": PlayerNote,
   "3391": ActorRestrictionsInformations,
   "7922": PlayerStatus,
   "9255": PlayerStatusExtended,
   "2130": ActorOrientation,
   "8641": EntityDispositionInformations,
   "7424": EntityMovementInformations,
   "1235": FightEntityDispositionInformations,
   "5501": GameContextActorInformations,
   "2634": GameContextActorPositionInformations,
   "5325": GameRolePlayTaxCollectorInformations,
   "1201": IdentifiedEntityDispositionInformations,
   "3674": MapCoordinates,
   "1411": MapCoordinatesAndId,
   "1105": MapCoordinatesExtended,
   "1156": TaxCollectorStaticExtendedInformations,
   "205": TaxCollectorStaticInformations,
   "4687": AbstractFightTeamInformations,
   "6596": BaseSpawnMonsterInformation,
   "2780": FightAllianceTeamInformations,
   "3080": FightCommonInformations,
   "5194": FightExternalInformations,
   "9": FightLoot,
   "8149": FightLootObject,
   "2083": FightOptionsInformations,
   "7905": FightResultAdditionalData,
   "2849": FightResultExperienceData,
   "3263": FightResultFighterListEntry,
   "3443": FightResultListEntry,
   "4801": FightResultMutantListEntry,
   "8644": FightResultPlayerListEntry,
   "398": FightResultPvpData,
   "2626": FightResultTaxCollectorListEntry,
   "7840": FightStartingPositions,
   "9065": FightTeamInformations,
   "1837": FightTeamLightInformations,
   "3689": FightTeamMemberCharacterInformations,
   "6520": FightTeamMemberEntityInformation,
   "697": FightTeamMemberInformations,
   "3828": FightTeamMemberMonsterInformations,
   "4581": FightTeamMemberTaxCollectorInformations,
   "2672": FightTeamMemberWithAllianceCharacterInformations,
   "6559": GameContextBasicSpawnInformation,
   "3563": GameContextSummonsInformation,
   "2861": GameFightAIInformations,
   "9900": GameFightCharacterInformations,
   "5027": GameFightCharacteristics,
   "470": GameFightEffectTriggerCount,
   "1134": GameFightEntityInformation,
   "6483": GameFightFighterEntityLightInformation,
   "690": GameFightFighterInformations,
   "7931": GameFightFighterLightInformations,
   "8085": GameFightFighterMonsterLightInformations,
   "2767": GameFightFighterNamedInformations,
   "7177": GameFightFighterNamedLightInformations,
   "4561": GameFightFighterTaxCollectorLightInformations,
   "9487": GameFightMonsterInformations,
   "3027": GameFightMonsterWithAlignmentInformations,
   "7944": GameFightMutantInformations,
   "3021": GameFightResumeSlaveInfo,
   "4199": GameFightSpellCooldown,
   "167": GameFightTaxCollectorInformations,
   "7811": SpawnCharacterInformation,
   "9037": SpawnCompanionInformation,
   "405": SpawnInformation,
   "2523": SpawnMonsterInformation,
   "3791": SpawnScaledMonsterInformation,
   "2649": AllianceInformations,
   "8950": AlternativeMonstersInGroupLightInformations,
   "1613": AnomalySubareaInformation,
   "1845": AtlasPointsInformations,
   "4259": BasicAllianceInformations,
   "489": BasicGuildInformations,
   "5227": BasicNamedAllianceInformations,
   "1906": GameRolePlayActorInformations,
   "4799": GameRolePlayCharacterInformations,
   "5866": GameRolePlayGroupMonsterInformations,
   "2209": GameRolePlayGroupMonsterWaveInformations,
   "1299": GameRolePlayHumanoidInformations,
   "3527": GameRolePlayMerchantInformations,
   "9718": GameRolePlayMountInformations,
   "9752": GameRolePlayMutantInformations,
   "419": GameRolePlayNamedActorInformations,
   "1050": GameRolePlayNpcInformations,
   "5987": GameRolePlayNpcWithQuestInformations,
   "7346": GameRolePlayPortalInformations,
   "743": GameRolePlayPrismInformations,
   "1810": GameRolePlayTreasureHintInformations,
   "5133": GroupMonsterStaticInformations,
   "5525": GroupMonsterStaticInformationsWithAlternatives,
   "7649": GuildInAllianceInformations,
   "2826": GuildInformations,
   "6597": HumanInformations,
   "1697": HumanOption,
   "255": HumanOptionAlliance,
   "7900": HumanOptionEmote,
   "44": HumanOptionFollowers,
   "6489": HumanOptionGuild,
   "6890": HumanOptionObjectUse,
   "6238": HumanOptionOrnament,
   "5177": HumanOptionSkillUse,
   "7073": HumanOptionSpeedMultiplier,
   "157": HumanOptionTitle,
   "9972": MonsterBoosts,
   "3301": MonsterInGroupInformations,
   "8269": MonsterInGroupLightInformations,
   "2912": ObjectItemInRolePlay,
   "1555": AlignmentWarEffortInformation,
   "4729": BreachBranch,
   "8289": BreachReward,
   "4455": ExtendedBreachBranch,
   "5736": ExtendedLockedBreachBranch,
   "925": ArenaLeagueRanking,
   "3258": ArenaRankInfos,
   "413": ArenaRanking,
   "1569": LeagueFriendInformations,
   "1740": DecraftedItemStackInfo,
   "5624": JobBookSubscription,
   "1811": JobCrafterDirectoryEntryJobInfo,
   "336": JobCrafterDirectoryEntryPlayerInfo,
   "10": JobCrafterDirectoryListEntry,
   "5830": JobCrafterDirectorySettings,
   "6378": JobDescription,
   "8463": JobExperience,
   "7349": MapNpcQuestInfo,
   "2868": DungeonPartyFinderPlayer,
   "7186": NamedPartyTeam,
   "4963": NamedPartyTeamWithOutcome,
   "5192": PartyGuestInformations,
   "7053": PartyInvitationMemberInformations,
   "1403": PartyMemberArenaInformations,
   "3797": PartyMemberGeoPosition,
   "7293": PartyMemberInformations,
   "3337": PartyEntityBaseInformation,
   "1645": PartyEntityMemberInformation,
   "4439": GameRolePlayNpcQuestFlag,
   "1716": QuestActiveDetailedInformations,
   "2561": QuestActiveInformations,
   "1202": QuestObjectiveInformations,
   "7979": QuestObjectiveInformationsWithCompletion,
   "8401": PortalInformation,
   "4912": TreasureHuntFlag,
   "5044": TreasureHuntStep,
   "277": TreasureHuntStepDig,
   "3878": TreasureHuntStepFight,
   "9440": TreasureHuntStepFollowDirection,
   "8970": TreasureHuntStepFollowDirectionToHint,
   "2724": TreasureHuntStepFollowDirectionToPOI,
   "3737": BidExchangerObjectInfo,
   "7038": ForgettableSpellItem,
   "8060": GoldItem,
   "6716": Item,
   "1090": ObjectEffects,
   "1144": ObjectItem,
   "2712": ObjectItemGenericQuantity,
   "1764": ObjectItemInformationWithQuantity,
   "886": ObjectItemMinimalInformation,
   "7100": ObjectItemNotInContainer,
   "5575": ObjectItemQuantity,
   "1032": ObjectItemQuantityPriceDateEffects,
   "7439": ObjectItemToSell,
   "3734": ObjectItemToSellInBid,
   "4115": ObjectItemToSellInHumanVendorShop,
   "8056": ObjectItemToSellInNpcShop,
   "6968": SellerBuyerDescriptor,
   "5286": SpellItem,
   "9999": ObjectEffect,
   "8986": ObjectEffectCreature,
   "8113": ObjectEffectDate,
   "2887": ObjectEffectDice,
   "5388": ObjectEffectDuration,
   "5031": ObjectEffectInteger,
   "502": ObjectEffectLadder,
   "4732": ObjectEffectMinMax,
   "3395": ObjectEffectMount,
   "2555": ObjectEffectString,
   "5440": EntityInformation,
   "7715": ProtectedEntityWaitingForHelpInfo,
   "8614": FinishMoveInformations,
   "8340": AbstractContactInformations,
   "7350": AcquaintanceInformation,
   "2998": AcquaintanceOnlineInformation,
   "2931": FriendInformations,
   "6579": FriendOnlineInformations,
   "522": FriendSpouseInformations,
   "8681": FriendSpouseOnlineInformations,
   "3826": IgnoredInformations,
   "4298": IgnoredOnlineInformations,
   "7288": Contribution,
   "9960": GuildEmblem,
   "3151": GuildMember,
   "5401": GuildRankInformation,
   "70": GuildRankMinimalInformation,
   "2314": GuildRankPublicInformation,
   "5802": HavenBagFurnitureInformation,
   "5249": ApplicationPlayerInformation,
   "976": GuildApplicationInformation,
   "324": GuildLogbookEntryBasicInformation,
   "1251": GuildLogbookChestActivity,
   "9284": GuildLevelUpActivity,
   "3725": GuildPaddockActivity,
   "5181": GuildPlayerFlowActivity,
   "5102": GuildPlayerRankUpdateActivity,
   "9683": GuildRankActivity,
   "8199": GuildUnlockNewTabActivity,
   "7615": GuildRecruitmentInformation,
   "403": AdditionalTaxCollectorInformations,
   "2378": TaxCollectorBasicInformations,
   "7396": TaxCollectorComplementaryInformations,
   "9488": TaxCollectorFightersInformation,
   "146": TaxCollectorGuildInformations,
   "7255": TaxCollectorInformations,
   "8279": TaxCollectorLootInformations,
   "7087": TaxCollectorMovement,
   "4172": TaxCollectorWaitingForHelpInformations,
   "7015": HavenBagRoomPreviewInformation,
   "4256": AccountHouseInformations,
   "6289": HouseGuildedInformations,
   "1082": HouseInformations,
   "5756": HouseInformationsForGuild,
   "3668": HouseInformationsForSell,
   "5175": HouseInformationsInside,
   "3926": HouseInstanceInformations,
   "7781": HouseOnMapInformations,
   "7456": Idol,
   "466": PartyIdol,
   "3496": InteractiveElement,
   "6640": InteractiveElementNamedSkill,
   "1464": InteractiveElementSkill,
   "3253": InteractiveElementWithAgeBonus,
   "5431": MapObstacle,
   "5825": StatedElement,
   "4309": SkillActionDescription,
   "1601": SkillActionDescriptionCollect,
   "9626": SkillActionDescriptionCraft,
   "7041": SkillActionDescriptionTimed,
   "2810": TeleportDestination,
   "5653": StorageTabInformation,
   "5533": UpdatedStorageTabInformation,
   "729": RecycledItem,
   "3447": EntityLook,
   "3771": IndexedEntityLook,
   "8816": SubEntity,
   "4082": ItemDurability,
   "9503": MountClientData,
   "32": UpdateMountBooleanCharacteristic,
   "4350": UpdateMountCharacteristic,
   "4473": UpdateMountIntegerCharacteristic,
   "967": MountInformationsForPaddock,
   "706": PaddockBuyableInformations,
   "8604": PaddockContentInformations,
   "8850": PaddockGuildedInformations,
   "7920": PaddockInformations,
   "6240": PaddockInformationsForSell,
   "6147": PaddockInstancesInformations,
   "1800": PaddockItem,
   "95": CharacterCharacteristicForPreset,
   "7295": EntitiesPreset,
   "2769": ForgettableSpellsPreset,
   "5449": FullStatsPreset,
   "1753": IconNamedPreset,
   "2551": IdolsPreset,
   "2797": ItemForPreset,
   "5024": ItemsPreset,
   "5250": Preset,
   "2486": PresetsContainerPreset,
   "1928": SimpleCharacterCharacteristicForPreset,
   "7670": SpellForPreset,
   "882": SpellsPreset,
   "5265": StatsPreset,
   "471": AllianceInsiderPrismInformation,
   "622": AlliancePrismInformation,
   "5465": PrismFightersInformation,
   "1260": PrismGeolocalizedInformation,
   "4160": PrismInformation,
   "7729": PrismSubareaEmptyInfo,
   "9291": Shortcut,
   "7402": ShortcutEmote,
   "3212": ShortcutEntitiesPreset,
   "8391": ShortcutObject,
   "4281": ShortcutObjectIdolsPreset,
   "7189": ShortcutObjectItem,
   "5702": ShortcutObjectPreset,
   "8039": ShortcutSmiley,
   "8014": ShortcutSpell,
   "4610": AbstractSocialGroupInfos,
   "1860": AlliancedGuildFactSheetInformations,
   "5647": AllianceFactSheetInformations,
   "570": GuildFactSheetInformations,
   "200": GuildInAllianceVersatileInformations,
   "766": GuildInsiderFactSheetInformations,
   "9976": GuildVersatileInformations,
   "3679": StartupActionAddObject,
   "6622": TrustCertificate,
   "7693": Version,
   "5420": BufferInformation
}
    
class TypesFactory:
    @classmethod
    def get_instance_id(cls,id,content):
        return id_class[str(id)](content)
    